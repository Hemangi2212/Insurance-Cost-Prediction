import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("Best_model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit page configuration
st.set_page_config(page_title="Insurance Cost Predictor 💸", page_icon="💰", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #faf9f6;
            padding: 2rem;
            border-radius: 15px;
        }
        .stButton>button {
            background-color: #00a896;
            color: white;
            border-radius: 8px;
            padding: 0.6em 1.2em;
            font-size: 1.1em;
            font-weight: 600;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #00796b;
            transform: scale(1.05);
        }
        h1, h2, h3 {
            color: #00796b;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            padding: 10px;
            border-top: 1px solid #ccc;
            color: #666;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.title("💸 Insurance Cost Prediction App")
st.markdown("### 🔍 *Predict your medical insurance charges instantly!*")
st.write("This app uses a trained **Linear Regression** model to predict estimated insurance costs based on user details.")

st.markdown("---")

# Input section
with st.container():
    st.header("🧾 Enter Your Details")

    sex = st.selectbox("👤 Sex", ["male", "female"])
    region = st.selectbox("🌎 Region", ["northeast", "northwest", "southeast", "southwest"])
    smoker = st.selectbox("🚬 Smoker", ["yes", "no"])

    # Encode categorical values
    sex_val = 1 if sex == "male" else 0
    smoker_val = 1 if smoker == "yes" else 0
    region_map = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}
    region_val = region_map[region]

    input_data = np.array([[sex_val, region_val, smoker_val]])

    st.markdown("")

    # Predict button
    if st.button("🔮 Predict Insurance Cost"):
        prediction = model.predict(input_data)
        st.success(f"💰 **Estimated Insurance Cost:** ${prediction[0]:.2f}")
        st.balloons()

st.markdown("---")

# About / Contact Info
with st.container():
    st.header("📞 Contact the Developer")
    st.markdown("""
    **👩‍💻 Developed by:** Hema Ransing  
    **📧 Email:** [hemaransing@gmail.com](mailto:hemaransing@gmail.com)  
    **📱 Mobile:** +91-9876543210  
    **💼 Role:** Fresher | Web Developer & Data Analytics Enthusiast  

    *Built with ❤️ using Streamlit and Machine Learning*
    """)

# Footer
st.markdown("""
    <div class="footer">
        © 2025 Hema Ransing | All Rights Reserved.
    </div>
""", unsafe_allow_html=True)
