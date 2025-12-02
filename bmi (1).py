import google.generativeai as genai
import streamlit as st

# Configure Gemini
genai.configure(api_key=st.secrets["Api_Key")
model = genai.GenerativeModel("gemini-2.5-flash")

# BMI Calculator
st.title("BMI Calculator with Nutritionist Advice")

# Take inputs from the user
name = st.text_input("Enter your name:")
wt = st.number_input("Enter your weight (kg):", min_value=0.0, format="%.2f")
ht = st.number_input("Enter your height (cm):", min_value=0.0, format="%.2f")

# Calculate BMI only if valid inputs
if wt > 0 and ht > 0:
    bmi = round(wt / (ht / 100) ** 2, 2)
    st.success(f"{name}, with your height {ht:.2f} cm and weight {wt:.2f} kg, your BMI is: {bmi}")

    # Prompt Gemini for expert nutritionist commentary
    prompt = f"Act like an expert nutritionist, comment on the BMI with the following data: height {ht} cm, weight {wt} kg, BMI {bmi}"
    response = model.generate_content(prompt)

    st.info(response.text)
else:
    st.warning("Please enter valid weight and height values.")







