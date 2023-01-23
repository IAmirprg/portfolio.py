import pandas
import streamlit as st

st.set_page_config(layout="wide")

col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])
with col1:
    st.image("images/amir.png")
with col2:
    st.title("Amir Moradi here!")
    content = """Hi, I'm Amir. I'm 20 years old , 
    I'm python programmer and interested in AI and robotics. 
    I study CE in university. I started programming from 2021 
    and after a long journey I prefer to write code with python
     cuz i like it and  it's quite simple and powerful """

    st.info(content)

content = """
below you can find some of the apps i have built in python feel free to
 contact me!"""
st.write(f"<h4>{content}</h4>",
         unsafe_allow_html=True)

col3, col4 = st.columns(2)
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source code]({row['url']})")
