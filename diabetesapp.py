import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="centered"
)
st.title("🩺 Diabetes Prediction")
st.write(
    "Enter the patient's information below to estimate "
    "the probability of diabetes."
)

#load trained pipeline
model=joblib.load("diabetes_logistic_pipeline.pkl")

col1, col2 = st.columns(2)
with col1:
    pregnancies = st.number_input(
        "Pregnancies",
        min_value=0,
        max_value=20,
        value=0
    )

    glucose = st.number_input(
        "Glucose",
        min_value=0.0,
        max_value=300.0,
        value=120.0
    )

    blood_pressure = st.number_input(
        "Blood Pressure",
        min_value=0.0,
        max_value=200.0,
        value=70.0
    )
    skin_thickness = st.number_input(
        "Skin Thickness",
        min_value=0.0,
        max_value=100.0,
        value=20.0
    )

with col2:
    insulin = st.number_input(
        "Insulin",
        min_value=0.0,
        max_value=1000.0,
        value=80.0
    )

    bmi = st.number_input(
        "BMI",
        min_value=0.0,
        max_value=100.0,
        value=32.0
    )

    diabetes_pedigree = st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.0,
        max_value=3.0,
        value=0.47
    )
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=33
    )



st.divider()
if st.button("Predict Diabetes", use_container_width=True):

    input_data = pd.DataFrame({
        "Pregnancies": [pregnancies],
        "Glucose": [glucose],
        "BloodPressure": [blood_pressure],
        "SkinThickness": [skin_thickness],
        "Insulin": [insulin],
        "BMI": [bmi],
        "DiabetesPedigreeFunction": [diabetes_pedigree],
        "Age": [age]
    })

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error("Prediction: Diabetes (Outcome = 1)")
    else:
        st.success("Prediction: No Diabetes (Outcome = 0)")

    st.metric(
        "Probability of Diabetes",
        f"{probability:.2%}"
    )
st.info(
    "This application is for educational purposes only "
    "and should not be used as a medical diagnosis."
)