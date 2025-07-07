import streamlit as st

st.title("Daily Exam Operations App")

st.header("Data Entry")

date = st.date_input("Date")
task = st.text_input("Task Description")

if st.button("Submit"):
    st.success(f"Data submitted:\nDate: {date}\nTask: {task}")
