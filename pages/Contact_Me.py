import streamlit as st

st.header("Contact me")

with st.form(key="my_form"):
    user_email = st.text_input("Your Email address:")
    user_message = st.text_area("Your message:")
    submit_button = st.form_submit_button("Submit")
