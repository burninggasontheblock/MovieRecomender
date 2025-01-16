import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from surprise import SVD
from surprise import Dataset
from surprise.model_selection import cross_validate
from flask import Flask, request, jsonify

# 1. Load and Preprocess Data
def load_data():
    # Use the MovieLens dataset (adjust path as needed)
    data = Dataset.load_builtin('ml-100k')
    return data

# 2. Train Collaborative Filtering Model
def train_model(data):
    trainset = data.build_full_trainset()
    algo = SVD()
    algo.fit(trainset)
    return algo

# 3. Evaluate Model
def evaluate_model(data, algo):
    cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

# 4. Predict Function
def get_recommendations(user_id, algo, n=10):
    try:
        # Convert user_id to inner ID
        inner_user_id = algo.trainset.to_inner_uid(user_id)
    except ValueError:
        return {"error": f"User ID {user_id} not found in the dataset."}

    recommendations = []
    for inner_item_id in algo.trainset.all_items():
        # Predict the rating
        pred = algo.predict(inner_user_id, algo.trainset.to_raw_iid(inner_item_id))
        recommendations.append((algo.trainset.to_raw_iid(inner_item_id), pred.est))

    # Sort recommendations by predicted rating in descending order
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations[:n]

# 5. Deployment with Flask
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to MovieReck!",
        "usage": "/recommend?user_id=<USER_ID>&n=<NUMBER_OF_RECOMMENDATIONS>"
    })

@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id')
    n = int(request.args.get('n', 10))

    if not user_id:
        return jsonify({'error': 'Please provide a user_id'}), 400

    recommendations = get_recommendations(user_id, algo, n)
    
    # Check if an error occurred
    if isinstance(recommendations, dict) and "error" in recommendations:
        return jsonify(recommendations), 400

    return jsonify({'user_id': user_id, 'recommendations': recommendations})

if __name__ == '__main__':
    # Load data and train model
    data = load_data()
    algo = train_model(data)
    evaluate_model(data, algo)

    # Run the Flask app
    app.run(debug=True)
