import streamlit as st
import yaml

st.set_page_config(
    page_title="MindfulMelodies",
    page_icon=":notes:",  
    layout="wide",
)

your_name = "Maria Bourbon"
school_name = "Ironhack Lisbon"
course_name = "Data Analytics"

st.sidebar.title("Info")
st.sidebar.write(f"Name: {your_name}")
st.sidebar.write(f"School: {school_name}")
st.sidebar.write(f"Course: {course_name}")
    
st.markdown(
    """
    <style>
        body {
            background-color: #2b4db7;  /* Background color */
            color: #fdfdff;  /* Text color */
        }
        .secondary-background-color {
            background-color: #1a1a1a;  /* Secondary background color */
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("MindfulMelodies: Your Musical Companion for Mental Well-being")

st.write("Thank you👋!")


image_url = "https://media.tenor.com/jfb3kQgSDnQAAAAd/sadness-sadness-inside-out.gif"

st.markdown(
    f'<div style="text-align:center;"><img src="{image_url}" alt="Image" style="width:600px;"></div>',
    unsafe_allow_html=True
)

st.write("Movie sugestion: Inside Out")


