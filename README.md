# MovieRecomender

MovieReck is a movie recommendation system built using collaborative filtering techniques. It leverages the MovieLens dataset to provide personalized movie recommendations based on user input.

## Features

- **Data Loading and Preprocessing:** Utilizes the MovieLens dataset for training.
- **Model Training:** Implements Singular Value Decomposition (SVD) for collaborative filtering.
- **Model Evaluation:** Evaluates the model's performance using RMSE and MAE metrics.
- **RESTful API:** Provides an easy-to-use interface for getting movie recommendations through a Flask web service.

## Prerequisites

Ensure you have the following packages installed:

- Flask
- pandas
- numpy
- surprise
- scikit-learn

You can install the required packages using pip:

```bash
pip install Flask pandas numpy scikit-learn surprise

Here's a README.md file created for your moviereck.py project:
markdownCopy code# MovieReck

MovieReck is a movie recommendation system built using collaborative filtering techniques. It leverages the MovieLens dataset to provide personalized movie recommendations based on user input.

## Features

- **Data Loading and Preprocessing:** Utilizes the MovieLens dataset for training.
- **Model Training:** Implements Singular Value Decomposition (SVD) for collaborative filtering.
- **Model Evaluation:** Evaluates the model's performance using RMSE and MAE metrics.
- **RESTful API:** Provides an easy-to-use interface for getting movie recommendations through a Flask web service.

## Prerequisites

Ensure you have the following packages installed:

- Flask
- pandas
- numpy
- surprise
- scikit-learn

You can install the required packages using pip:

```bash
pip install Flask pandas numpy scikit-learn surprise
Getting Started


Clone the Repository:
bashCopy codegit clone <repository-url>
cd <repository-directory>


Run the Application:
bashCopy codepython moviereck.py


Access the API:
Open your web browser and go to http://127.0.0.1:5000/ to see the welcome message and usage instructions.


Get Recommendations:
To get movie recommendations, use the following endpoint:
GET /recommend?user_id=<USER_ID>&n=<NUMBER_OF_RECOMMENDATIONS>

Replace <USER_ID> with the user's ID and <NUMBER_OF_RECOMMENDATIONS> with the desired number of recommendations (default is 10).


Code Structure

load_data(): Loads and preprocesses the MovieLens dataset.
train_model(data): Trains the collaborative filtering model using SVD.
evaluate_model(data, algo): Evaluates the model's performance using cross-validation.
get_recommendations(user_id, algo, n): Generates movie recommendations based on the provided user ID.
Flask API endpoints:

/: Displays the welcome message and usage instructions.
/recommend: Takes user ID and number of recommendations as parameters and returns the movie recommendations.



License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

MovieLens for providing the dataset.
Surprise for the collaborative filtering library.
