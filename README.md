## Churn_prediction_Deployment

Objective: Customer churn occurs when customers stop doing business with a company. The objective of this project is to estimate whether a bank's customers leave the bank or not.

Dataset: The Bank customer dataset contains customer’s details and has both numerical and categorical columns.

Tasks and Steps:

The steps that will be taken are:

1. Data Analysis: Analyse the data to evaluate it, performed some metrics

2. Data Pre-Processing: Removed the unused column, feature scaling

3. Model Creation: Created K Means clustering model to predict churn rate. 

4. API Creation: Created application using flask

5. Deployment: Deployed the application on Heroku using Docker.

## Docker
- Docker installation

- Create the Dockerfile to build the image and run the Flask application

- Build the Docker image

docker build -t flask-heroku-first

docker run -d -p 5000:5000 flask-heroku-first

## App Deployment to Heroku
- Create the container onto Heroku

heroku container:push web --app churn-prediction-ml


- release the container
heroku container:release web --app churn-prediction-ml


## Required libraries: 
For running the code we need to install the following libraries:

1. pandas

2. Numpy

3. Seaborn

4. Matplotlib

5. Sklearn
