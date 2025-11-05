import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("Best_model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit App
st.set_page_config(page_title="Insurance Cost Prediction", page_icon="💸", layout="centered")

st.title("💸 Insurance Cost Prediction App")
st.write("This app predicts **medical insurance charges** using a trained Linear Regression model.")

st.markdown("---")

# Sidebar inputs
st.sidebar.header("User Input Features")

age = st.sidebar.number_input("Age", min_value=1, max_value=100, value=25)
sex = st.sidebar.selectbox("Sex", ["male", "female"])
bmi = st.sidebar.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=60.0, value=24.5)
children = st.sidebar.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.sidebar.selectbox("Smoker", ["yes", "no"])
region = st.sidebar.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Encoding categorical values
sex_val = 1 if sex == "male" else 0
smoker_val = 1 if smoker == "yes" else 0
region_map = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}
region_val = region_map[region]

# Prepare data for prediction
input_data = np.array([[age, bmi, children, sex_val, smoker_val, region_val]])

# Predict button
if st.button("🔮 Predict Insurance Cost"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Insurance Cost: **${prediction[0]:.2f}**")

st.markdown("---")
st.caption("Developed by Hema using Streamlit & Machine Learning 💻")
