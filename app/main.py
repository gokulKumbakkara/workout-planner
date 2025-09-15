import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from app.langchain.helper import generate_workout_plans

st.title("Workout Plan Generator")

# Sidebar muscle group selector
muscle_group = st.sidebar.selectbox(
    "Pick a muscle group",
    ("Chest", "Shoulder", "Triceps", "Back", "Biceps", "Legs", "Abs")
)

if muscle_group:
    response = generate_workout_plans(muscle_group)

    # Show workout plan
    st.header(f"Workout Plan for {response['muscle_group']}")
    st.write(response["workout_plan"].strip())

    # Show number of sets
    no_of_sets = response["no_of_sets"].strip().split(",")
    st.subheader("Recommended Sets")
    for item in no_of_sets:
        st.write("-", item.strip())
