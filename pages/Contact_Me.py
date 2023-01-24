import streamlit as st
from Send_Email import send_email

st.header("Contact me")

with st.form(key="my_form"):
    user_email = st.text_input("Your email address:")
    user_message = st.text_area("Your message:")
    message = f"""\
Subject:New email from {user_email}

From: {user_email}
{user_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully!")



