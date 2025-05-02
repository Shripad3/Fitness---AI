import streamlit as st
import function
import time

st.set_page_config(page_title="AI Fitness Coach", layout="centered")

st.title("💪 Personalized Diet & Workout Planner")

with st.form("user_form"):
    name = st.text_input("Name")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    age = st.number_input("Age", min_value=5, max_value=100, step=1)
    weight = st.number_input("Weight (kg)", min_value=20, max_value=200, step=1)
    height = st.number_input("Height (cm)", min_value=100, max_value=250, step=1)
    food_preference = st.selectbox("Food Preference", ["Vegetarian", "Vegan", "Non-Vegetarian", "Eggetarian"])
    goal = st.text_input("What is your fitness goal?")

    submitted = st.form_submit_button("Generate Plan")

if submitted:
    with st.spinner("Generating your personalized plan..."):
        time_start = time.time()

        prompt_text = f'''
        My name is {name}. I am a {int(age)} year old {gender}.
        My weight is {int(weight)}, my height is {int(height)} and I prefer {food_preference} food.
        Give me a detailed diet plan and a workout plan to achieve this goal ({goal}).
        '''
        response = function.ask_gemini(prompt_text)

        st.markdown("### 📝 Your Personalized Plan")
        st.markdown(response)

        time_end = time.time()
        st.success(f"Generated in {round(time_end - time_start, 2)} seconds.")
