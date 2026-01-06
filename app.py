import streamlit as st
import pandas as pd
import joblib

model = joblib.load('logistic_regression_heart.pkl')
scaler = joblib.load('scaler.pkl')
expected_columns = joblib.load('columns.pkl')

st.title("Heart Disease Prediction by Diganta❤️")
st.markdown("Provide the following details")

age = st.slider("Age", 18, 100, 40)
sex = st.selectbox("Sex", ['Male', 'Female'])
chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol = st.number_input("Cholesterol (mg/dl)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ['Yes', 'No'])
resting_ecg = st.selectbox("Resting ECG", ['Normal', 'ST', 'LVH'])
max_hr = st.number_input("Max Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox("Exercise Induced Angina", ['Yes', 'No'])
oldpeak = st.number_input("Oldpeak", 0.0, 10.0, 1.0)
st_slope = st.selectbox("ST Slope", ['Up', 'Flat', 'Down'])

if st.button("Predict"):

    raw_input = {col: 0 for col in expected_columns}

    raw_input['Age'] = age
    raw_input['RestingBP'] = resting_bp
    raw_input['FastingBS'] = 1 if fasting_bs == 'Yes' else 0
    raw_input['MaxHR'] = max_hr
    raw_input['Oldpeak'] = oldpeak

    if sex == 'Male':
        raw_input['Sex_M'] = 1

    if chest_pain == 'ATA':
        raw_input['ChestPainType_ATA'] = 1
    elif chest_pain == 'NAP':
        raw_input['ChestPainType_NAP'] = 1

    if resting_ecg == 'Normal':
        raw_input['RestingECG_Normal'] = 1
    elif resting_ecg == 'ST':
        raw_input['RestingECG_ST'] = 1

    if exercise_angina == 'Yes':
        raw_input['ExerciseAngina_Y'] = 1

    if st_slope == 'Flat':
        raw_input['ST_Slope_Flat'] = 1
    elif st_slope == 'Up':
        raw_input['ST_Slope_Up'] = 1

    if resting_bp >= 140:
        raw_input['RestingBPlevel_Hypertension Stage 2'] = 1

    if 200 <= cholesterol < 240:
        raw_input['CholesterolLevel_Borderline High'] = 1
    elif cholesterol >= 240:
        raw_input['CholesterolLevel_High'] = 1

    input_df = pd.DataFrame([raw_input])[expected_columns]

    scaled_input = pd.DataFrame(
        scaler.transform(input_df),
        columns=expected_columns
    )
    prediction = model.predict(scaled_input)[0]

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")