
import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

st.title("BMI Calculator")
st.write("Enter your weight in kilograms and height in meters.")

weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1, format="%.2f")
height = st.number_input("Height (m)", min_value=0.0, step=0.01, format="%.2f")

if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = weight / (height * height)
        st.success(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            st.info("Category: Underweight")
        elif bmi < 25:
            st.info("Category: Normal weight")
        elif bmi < 30:
            st.info("Category: Overweight")
        else:
            st.info("Category: Obese")
    else:
        st.error("Please enter valid weight and height values.")

bmi = weight / (height * height)
