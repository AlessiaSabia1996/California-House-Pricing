# CaliforniaHousing
Prediction model for house pricing - prediction available as request through API or command line

# Dataset
Number of Instances: 20640

Number of Attributes: 8 numeric, predictive attributes and the target

Attribute Information:
    - MedInc        median income in block group
    - HouseAge      median house age in block group
    - AveRooms      average number of rooms per household
    - AveBedrms     average number of bedrooms per household
    - Population    block group population
    - AveOccup      average number of household members
    - Latitude      block group latitude
    - Longitude     block group longitude

Missing Attribute Values: None

# Project technologies: Python, scikit-learn, flask, click
# Objective of the project: House price prediction
# Project description:

Phase 1: Data exploration (filename: data_exploration.ipynb)
In this phase, a jupyter notebook is used to do a preliminar exploratory analysis of the data. 
In particular, during this phase, the kind of model to use is choosen based on the data characteristics, data values falls in different range so Scaling will be necessary.
Linear correlations is tested between some of the features, not linear correlation is found so **SVR regressor** is used as a model.

Phase 2: Model building (filename: train.py)
In this phase, data scaling is performed using StandardScaler from scikit-lean.
The model is then build and trained, evaluation metrics are **r2_score** and **mean_absolute_error**

Phase 3: Model prediction (filename: prediction.py)
Features to pass: Insert income, house age, number of rooms, number of bedrooms, population, number of household members, latitude, longitude
In this phase, click library is used to be able to make predictions using command line passed features, otherwise activating the api it is possible to pass the features through a post request (example: curl -X POST http://127.0.0.1:5000/predict \     -H "Content-Type: application/json" \     -d '{"features": [8.3252, 41, 6.984127, 1.02381, 322, 2.555556, 37.88, -122.23]}'  )

Phase 4: project packaging
Using **setuptools** the project is packaged and ready to be installed.
To install the project, in the project folder open a terminal and paste -> pip install -e .     
Features to pass: Insert income, house age, number of rooms, number of bedrooms, population, number of household members, latitude, longitude
Run the prediction using -> predict-price --features pass here the features
