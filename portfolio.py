import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image("images/amir.png")
with col2:
    st.title("Amir Moradi")
    content = """Hi, I'm Amir. I'm 20 years old , 
    I'm python programmer and interested in AI and robotics. 
    I study CE in university. I started programming from 2021 
    and after a long journey I prefer to write code with python
     cuz i like it and  it's quite simple and powerful """

    st.info(content)
