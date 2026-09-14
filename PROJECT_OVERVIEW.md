# Forest Fire Prediction – Project Overview

## Project Objective
This project helps estimate wildfire risk using weather and forest condition data.  
It predicts:
- the chance of a fire happening
- the possible burned area if a fire is likely

The goal is to support faster decision-making for early warning and prevention planning.

## Tech Used
- **Python**: core programming language
- **Flask**: web app framework to take user input and show predictions
- **TensorFlow/Keras**: loads trained machine learning models
- **Scikit-learn (saved scalers)**: prepares input data in the same format used during training
- **Pandas**: organizes input data into table form for model use
- **NumPy**: handles numeric calculations and reverse log transformation
- **Plotly**: shows a visual graph of predicted burned area
- **HTML/CSS/Bootstrap/JavaScript**: front-end interface for users

## Workflow (Simple)
1. User enters weather and forest indicators (temperature, humidity, wind, rainfall, FFMC, DMC, DC, ISI, month, day).
2. The app converts and formats this data.
3. Classification model predicts fire probability.
4. If risk is high, regression model predicts burned area.
5. Results are shown as a clear summary and a chart.

## Algorithm / Model
This project uses a **two-model pipeline**:
- **Model 1: Classification model** – predicts whether fire is likely or not.
- **Model 2: Regression model** – predicts how large the burned area could be.

A probability threshold is used to decide whether to run the burned-area prediction.

## Brief Explanation (Resume-Friendly)
Built an end-to-end wildfire risk prediction web application that combines machine learning and an interactive dashboard. The system takes environmental inputs, predicts fire likelihood, and estimates potential damage area to provide practical decision support for wildfire awareness and planning.
