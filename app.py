import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

st.title("BMI Calculator")
st.write("Enter your weight in kilograms and height in meters.")

weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1, format="%.2f")
height = st.number_input("Height (m)", min_value=0.0, step=0.01, format="%.2f")

if st.button("Calculate BMI"):
    if weight <= 0:
        st.error("Please enter a weight greater than 0.")
    elif height <= 0:
        st.error("Please enter a height greater than 0.")
    else:
        bmi = weight / (height * height)
        st.success(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            st.info("Category: Underweight")
        elif bmi < 25:
            st.info("Category: Normal weight")
        elif bmi < 30:
            st.warning("Category: Overweight")
        else:
            st.error("Category: Obese")

  
