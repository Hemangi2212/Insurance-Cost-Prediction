import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("Best_model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit page setup
st.set_page_config(page_title="💸 Insurance Cost Predictor", page_icon="💰", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #fdfcfb;
            padding: 2rem;
            border-radius: 12px;
        }
        h1, h2, h3 {
            color: #00695c;
        }
        .stButton>button {
            background-color: #009688;
            color: white;
            font-weight: 600;
            border-radius: 10px;
            transition: 0.3s;
            padding: 0.6em 1.2em;
        }
        .stButton>button:hover {
            background-color: #00796b;
            transform: scale(1.05);
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            padding: 15px;
            border-top: 1px solid #ccc;
            color: #555;
            font-size: 0.9em;
        }
    </style>
""", unsafe_allow_html=True)

# App header
st.title("💸 Insurance Cost Prediction App")
st.markdown("### 🔍 *Predict your medical insurance cost instantly!*")
st.write("This app uses a **Linear Regression model** trained on 3 key factors to estimate insurance charges:")

st.markdown("""
- 👤 **Sex**
- ⚖️ **BMI (Body Mass Index)**
- 🚬 **Smoker Status**
""")

st.markdown("---")

# Input Section
st.header("🧾 Enter Your Details")

sex = st.selectbox("👤 Select Sex", ["male", "female"])
bmi = st.number_input("⚖️ Enter BMI (Body Mass Index)", min_value=10.0, max_value=60.0, value=25.0)
smoker = st.selectbox("🚬 Are you a Smoker?", ["yes", "no"])

# Encode inputs
sex_val = 1 if sex == "male" else 0
smoker_val = 1 if smoker == "yes" else 0

# Prepare data for prediction
input_data = np.array([[sex_val, bmi, smoker_val]])

# Predict button
if st.button("🔮 Predict Insurance Cost"):
    prediction = model.predict(input_data)
    st.success(f"💰 **Estimated Insurance Cost:** ${prediction[0]:.2f}")
    st.balloons()

st.markdown("---")

# Contact Section
st.header("📞 Contact the Developer")
st.markdown("""
**👩‍💻 Developed by:** Hema Ransing  
**📧 Email:** [hemaransing@gmail.com](mailto:hemaransing@gmail.com)  
**📱 Mobile:** +91-9876543210  
**💼 Role:** Fresher | Web Developer & Data Analytics Enthusiast  

*Built with ❤️ using Streamlit and Machine Learning.*
""")

# Footer
st.markdown("""
    <div class="footer">
        © 2025 Hema Ransing | All Rights Reserved.
    </div>
""", unsafe_allow_html=True)
