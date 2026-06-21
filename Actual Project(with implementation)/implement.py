import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("implement_model.pkl")

st.title("Student Placement Predictor")

# Input fields
study_hours = st.number_input("Study Hours", min_value=0.0)
attendance = st.number_input("Attendance (%)", min_value=0.0, max_value=100.0)
sleep_hours = st.number_input("Sleep hour", min_value=0.0)
internet_usage = st.number_input("Internet Usage", min_value=0.0)
assignments_completed = st.number_input("Assignments Completed", min_value=0.0)
previous_score = st.number_input("Previous Score", min_value=0.0)


if st.button("Predict"):

    # Put features in SAME ORDER used during training
    data = pd.DataFrame({
        "study_hours": [study_hours],
        "attendance": [attendance],
        "sleep_hours": [sleep_hours],
        "internet_usage": [internet_usage],
        "assignments_completed": [assignments_completed],
        "previous_score": [previous_score]
    })

    prediction = model.predict(data)
    
    if prediction == 1:
        st.success("Predicions  Placed")
    else:
        st.success("Predicions  Not Placed")