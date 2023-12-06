import streamlit as st
from typing import List
import wikipediaapi
from streamlit_searchbox import st_searchbox


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

st.subheader("Introduction")

st.write("""
Embark on a transformative journey with MindfulMelodies, a specialized tool meticulously crafted to support your mental health through the beneficial influence of music.

**Project Phases:**

**1. Data Cleaning and Visualization:**
I begin by ensuring the integrity of the dataset, eliminating null values, and streamlining irrelevant data. Visualizations such as plots and heatmaps guide my analysis, revealing correlations crucial to understanding the impact of variables on mental health.

**2. Spotify Playlist Integration:**
MindfulMelodies leverages the Spotify API to curate playlists tailored to specific mental health conditions. Each playlist is thoughtfully selected to include genres known to have positive effects, providing a unique and personalized musical experience.

**User-Friendly:**
- **Personalized Playlists:** Select your mental health condition (OCD, Depression, Anxiety, or Insomnia) to discover curated playlists designed to uplift and support.
- **Explore & Connect:** Dive into the top playlists, each associated with a range of genres. A simple button click seamlessly connects you to the Spotify playlist of your choice.

MindfulMelodies is not just a tool, it's a companion on your mental health journey, offering quick and meaningful insights to help you make informed choices about the music that resonates with you.

Discover the profound impact of music on mental well-being with MindfulMelodies.
""")


col1, col2 = st.columns([2, 1])

col1.subheader("Search: \n The definition of each mental health condition or symptom listed in the tool, including OCD, depression, anxiety, and insomnia.\n")

with col1:
    wiki_wiki = wikipediaapi.Wikipedia("en", headers={"User-Agent": "http://localhost:8501/Introduction"})
    
    def search_wikipedia(searchterm: str) -> List[any]:
        page_py = wiki_wiki.page(searchterm)
        if page_py.exists():
            return [page_py.title, page_py.text]
        else:
            return []

    selected_value = st.text_input("Search Wikipedia")

    if selected_value:
        result = search_wikipedia(selected_value)
        if result:
            title, content = result
            st.header(title)
            st.write(content)

image_url = "https://upload.wikimedia.org/wikipedia/commons/6/61/Wikipedia-logo-transparent.png"  
col2.image(image_url, caption=" ", width=400)


