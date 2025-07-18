# app.py

import streamlit as st
import numpy as np
import joblib 

model = joblib.load('credit_fraud_model_fixed.joblib')

st.set_page_config(page_title="Credit Card Fraud Detector", layout="centered")
st.title("💳 Credit Card Fraud Detection")

st.subheader("Enter transaction details")

# Feature names
feature_names = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']

# Input fields
input_values = []
for feature in feature_names:
    val = st.number_input(f"{feature}", format="%.6f")
    input_values.append(val)

input_array = np.array(input_values).reshape(1, -1)

if st.button("Predict Fraud"):
    result = model.predict(input_array)
    if result[0] == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:
        st.success("✅ Legitimate Transaction")
