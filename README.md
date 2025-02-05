# Shield Insurance Premium Prediction

**➡️ [Explore the Live App Here](https://health-insurance-price-prediction.streamlit.app/)**

## Project Overview
This project aims to develop a predictive model for Shield Insurance to estimate health insurance premiums based on various factors such as age, smoking habits, BMI, and medical history. The objective is to create a high-accuracy model where the difference between the predicted and actual value on a minimum of 95% of the errors should be less than 10%. The final model is deployed using Streamlit for easy accessibility.

## Tech Stack
- **Programming Language**: Python  
- **Framework**: Streamlit  
- **Libraries & Tools**:
  - Scikit-learn
  - Pandas
  - NumPy
  - Seaborn
  - Matplotlib
  - Joblib (for model serialization)

## Algorithms Used
- Linear Regression
- Ridge Regression
- XGBoost Regressor

## Evaluation Metrics
- R² Score
- Mean Squared Error (MSE)

## End-to-End Implementation
1. **Data Collection** – Gathering relevant health insurance data.
2. **Data Cleaning** – Handling missing values, outlier treatment, and normalization.
3. **Feature Engineering** – Creating meaningful features to enhance model performance, including one-hot encoding, label encoding, and generating new features based on existing independent variables.
4. **Model Training & Fine-tuning** – Training different models and optimizing hyperparameters.
5. **Error Analysis** – Analyzing the distribution of error percentage between predicted and actual values.
6. **Model Segmentation** – Developed two models: one for age ≤ 25 and another for age > 25 to reduce error and increase prediction accuracy.
7. **Acquiring More Data & Retraining** – Enhancing model accuracy with additional data.
8. **Building & Deploying the App** – Developing an interactive UI using Streamlit for users to input data and receive premium predictions.

## Deployment
The final model is integrated into a Streamlit web application for real-time predictions. The app provides an intuitive interface where users can input their details and receive an estimated insurance premium instantly.




---
*I have completed this project as a part of the Codebasics Machine Learning Course.*
*Feel free to contribute or raise issues for improvements!*







