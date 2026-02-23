import streamlit as st
from prediction_helper import predict

st.title("Insurance Premium Predictor")

categorical_options = {
    "gender": ['Male', 'Female'],
    "region": ['Northeast', 'Northwest', 'Southeast', 'Southwest'],
    "marital_status": ['Unmarried', 'Married'],
    "bmi_category": ['Overweight', 'Underweight', 'Normal', 'Obesity'],

    # ✅ UI friendly name — preprocessing will map it
    "smoking_status": ['Regular', 'No Smoking', 'Occasional'],

    "employment_status": ['Self-Employed', 'Freelancer', 'Salaried'],
    "income_level": ['> 40L', '<10L', '10L - 25L', '25L - 40L'],
    "insurance_plan": ['Silver', 'Bronze', 'Gold']
}

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100)
with row1[1]:
    number_of_dependants = st.number_input('Dependants', min_value=0, step=1, max_value=5)
with row1[2]:
    region = st.selectbox("Region", categorical_options["region"])

with row2[0]:
    income_lakhs = st.number_input('Income (Lakhs)', min_value=0, step=1, max_value=100)
with row2[1]:
    marital_status = st.selectbox("Marital Status", categorical_options["marital_status"])
with row2[2]:
    gender = st.selectbox("Gender", categorical_options["gender"])

with row3[0]:
    genetical_risk = st.number_input('Genetical Risk', min_value=0, step=1, max_value=5)
with row3[1]:
    smoking_status = st.selectbox("Smoking Status", categorical_options["smoking_status"])
with row3[2]:
    bmi_category = st.selectbox("BMI Category", categorical_options["bmi_category"])

with row4[0]:
    medical_history = st.number_input('Medical History', min_value=0, step=1, max_value=20)
with row4[1]:
    employment_status = st.selectbox("Employment", categorical_options["employment_status"])
with row4[2]:
    insurance_plan = st.selectbox("Insurance Plan", categorical_options["insurance_plan"])

input_dict = {
    'age': age,
    'number_of_dependants': number_of_dependants,
    'region': region,
    'income_lakhs': income_lakhs,
    'marital_status': marital_status,
    'gender': gender,
    'genetical_risk': genetical_risk,
    'smoking_status': smoking_status,
    'bmi_category': bmi_category,
    'medical_history': medical_history,
    'employment_status': employment_status,
    'insurance_plan': insurance_plan
}

if st.button('Predict Premium'):
    prediction = predict(input_dict)
    st.success(f"Predicted Premium: {prediction}")
