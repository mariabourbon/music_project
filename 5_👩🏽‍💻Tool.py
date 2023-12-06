import streamlit as st
from PIL import Image
import requests
import io
import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import getpass
    
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


col1, col2 = st.columns([2, 1]) 


col1.write("""After you logged in to our account on MindfulMelodies, you have acess to the tool. \n 
Now to use you only have to chose the mental health problem you're facing and it will show you a list of playlists chosen just for you, with the button to go listen to them in Spotify!
Explore and find the perfect soundtrack for a healthier and happier you!""")
image_url = "https://www.research4life.org/wp-content/uploads/2019/04/Canva-Person-Using-Macbook-Air.jpg"  
col2.image(image_url, caption="   ",width=400)


CLIENT_ID = "451a3679cec64f3b97b14beb667a5529"
CLIENT_SECRET = "cb7ce96344174fb389e92cb293ce1952"
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

mental_health_genres = {
    'Anxiety': ["Lo-fi", "Jazz", "Latin", "Country"],
    'Depression': ["Lo-fi", "Jazz", "Latin", "Country"],
    'Insomnia': ["Lo-fi", "Gospel"],
    'OCD': ["Lo-fi", "Jazz", "Latin", "Country"]
}

def open_url(url):
    webbrowser.open(url)

def display_playlists(chosen_issue):
    genres = mental_health_genres.get(chosen_issue, [])

    if genres:
        for genre in genres:
            try:
                playlists = sp.search(q=f"{genre}", type='playlist', limit=1)

                if 'playlists' in playlists and 'items' in playlists['playlists']:
                    if playlists['playlists']['items']:
                        playlist = playlists['playlists']['items'][0]

                        # Organize layout with playlist info on the left and image on the right
                        col1, col2 = st.columns(2)

                        # Display playlist information on the left
                        col1.text(f"Playlist for genre {genre}:\n"
                                  f"{playlist['name']}\n"
                                  f"   Playlist URL: {playlist['external_urls']['spotify']} ({genre} genre)\n")

                        # Handle the image retrieval on the right
                        try:
                            image_data = requests.get(playlist['images'][0]['url'], stream=True).content
                            image = Image.open(io.BytesIO(image_data))
                            # Adjust the size of the image to be smaller
                            image = image.resize((90, 90), Image.LANCZOS)
                            col2.image(image, caption=f"Top playlist for {genre}", use_column_width=False)
                        except Exception as e:
                            st.text(f"Error: {e}")

                        # Button to open the playlist URL
                        col1.button(f"Open Playlist ({genre})", on_click=lambda u=playlist['external_urls']['spotify']: open_url(u))
                        col1.text("\n")
                    else:
                        st.text(f"No playlist found for {genre}\n")
                else:
                    st.text("Error retrieving playlist information.\n")
            except spotipy.SpotifyException as e:
                st.text(f"Error: {e}\n")
    else:
        st.text(f"Genres not found for the selected mental health issue: {chosen_issue}\n")

def main():
    st.title("Playlists")

    chosen_issue = st.selectbox("Choose your mental health issue or symptom: ", list(mental_health_genres.keys()))

    if st.button("Search Playlists"):
        st.header(f"Playlists for {chosen_issue}")
        display_playlists(chosen_issue)

if __name__ == "__main__":
    main()
    
st.text("Hope you found some great musics that will help you feel better!")
