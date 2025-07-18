# app.py

import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('C:/Users/prudh/OneDrive/Desktop/Machine Learning/Projects/Credit Card Fraud Detection/card.sav', 'rb') as file:
    model = pickle.load(file)

st.set_page_config(page_title="Credit Card Fraud Detector", layout="centered")
st.title("💳 Credit Card Fraud Detection")

st.subheader("Enter transaction details")

# Define all feature names (adjust if your model uses different ones)
feature_names = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']

# Create input fields
input_values = []
for feature in feature_names:
    val = st.number_input(f"{feature}", format="%.6f")
    input_values.append(val)

# Convert input to NumPy array
input_array = np.array(input_values).reshape(1, -1)

# Predict
if st.button("Predict Fraud"):
    result = model.predict(input_array)
    if result[0] == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:
        st.success("✅ Legitimate Transaction")
