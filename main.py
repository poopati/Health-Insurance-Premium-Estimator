import streamlit as st
from prediction_helper import predict

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns([1, 2, 1])  # Wider middle column
with col2:
    st.title("Health Insurance Premium Estimator")

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Income Level': ['<10L', '10L - 25L', '> 40L', '25L - 40L'],
    'Medical History': [
        'Diabetes', 'High blood pressure', 'No Disease',
        'Diabetes & High blood pressure', 'Thyroid', 'Heart disease',
        'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Create four rows of three columns each

row1 = st.columns(6)
row2 = st.columns(6)
row3 = st.columns(6)
row4 = st.columns(6)
row5 = st.columns(6)
row6 = st.columns([1,2,1,1,1])


# Assign inputs to the grid
with row1[1]:
    age = st.number_input('Age', min_value=18, step= 1, max_value=100)
with row1[2]:
    employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])
with row1[3]:
    income_level = st.selectbox('Income Level', categorical_options['Income Level'])
with row1[4]:    
    income_lakhs = st.number_input('Income in Lakhs', min_value= 0 , step =1, max_value=200)

with row2[1]:
    gender= st.selectbox('Gender', categorical_options['Gender'])
with row2[2]:
    marital_status = st.selectbox('Marital Status', categorical_options['Marital Status']) 
with row2[3]:
    number_of_dependants = st.number_input('Number of Dependants', min_value= 0 , step =1, max_value=20)
with row2[4]:
    region = st.selectbox('Region', categorical_options['Region'])


with row3[1]:
    bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])
with row3[2]:
    smoking_status= st.selectbox('Smoking Status', categorical_options['Smoking Status'])
with row3[3]:
    genetical_risk = st.number_input('Genetical Risk', min_value=0, step= 1, max_value=5)
with row3[4]:
    medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

with row4[1]:
    insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])



# create a dictionary for input values
input_dict = {
    'Age': age, 
    'Number of Dependants':number_of_dependants,
    'Income Level': income_level,
    'Income Lakhs':income_lakhs, 
    'Genetical Risk':genetical_risk,
    'Insurance Plan':insurance_plan,
    'Employment Status':employment_status,
    'Gender':gender,
    'Marital Status':marital_status,
    'BMI Category':bmi_category,
    'Smoking Status':smoking_status,
    'Region':region,
    'Medical History':medical_history
}

# Button to make prediction
with row6[1]:
    if st.button('Predict'):
        prediction = predict(input_dict)
        st.success(f'The estimated Health Insurance Cost is: {round(prediction[0])} INR')
