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


col1, col2 = st.columns([3, 1]) 


col1.write("""Welcome to my website!

Today, I'm excited to introduce you to my latest project, HarmonyHealing.\n
Behind the scenes, I've been working on cleaning, manipulating and analyzing data from a Kaggle survey.\n 
This survey dives deeply into the ways in which people dealing with mental health issues relate to various musical genres.\n

Why is this significant?\n
Well, it's the basis for the amazing tool that I have created.\n
Picture this: you choose your specific mental health experience, and just like that, the tool guides you to the music genre that resonates with your unique journey.

Stay tuned as I delve further into this project. 
I'm thrilled to have you on board👋!
""")


image_url = "https://static01.nyt.com/images/2019/09/26/smarter-living/26_gubar_music/26_gubar_music-articleLarge.jpg"  
col2.image(image_url, caption="   ",width=400)



canva_embed_code = "<https://www.canva.com/design/DAF2JcdF7WA/2RkIpGowthq80ZqzbN2LRw/view?mode=prototype>"
st.markdown(f'[App Presentation]({canva_embed_code})', unsafe_allow_html=True)




