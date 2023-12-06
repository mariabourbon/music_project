import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

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

music = pd.read_csv('music_data_frame.csv', sep=';')

st.title("MindfulMelodies: Your Musical Companion for Mental Well-being")
st.header("Data Analysis and Visualization")


row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    st.subheader("Dataset")
    st.dataframe(music)
with row1_col2:
    st.subheader("Notes")
    st.write( "My dataset contained some columns that didn't have relevant data such as: Timestamp and Permissions. "
              "Also had to drop some null values and look at the outliers, that showed in Hours per day, BPM, and Age. "
              "Some important definitions of the columns are:\n "
              "- **Hours per day**: Number of hours the respondent listens to music per day\n"
              "- **Fav genre**: Respondent's favorite or top genre\n"
              "- **Frequency [Classical/Country/EDM/Folk/Gospel/Hip Hop/Jazz/K pop/ Latin/Lofi/Metal/Pop/R&B/Rap/Rock/Video game music]**: How frequently the respondent listens to classical music\n"
              "- **Anxiety**: Self-reported anxiety, on a scale of 0-10\n"
              "- **Depression**: Self-reported depression, on a scale of 0-10\n"
              "- **Insomnia**: Self-reported insomnia, on a scale of 0-10\n"
              "- **OCD**: Self-reported OCD, on a scale of 0-10\n"
              "- **Music effects**: Does music improve/worsen the respondent's mental health conditions?\n"
)


row2_col1, row2_col2 = st.columns(2)
with row2_col1:
    st.subheader("Correlation Heatmap")
    corr = music[["Age", "Hours per day", "BPM", "Anxiety", "Depression", "Insomnia", "OCD"]].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    st.pyplot()
with row2_col2:
    st.subheader("Insights")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write(
             " - There is a strong direct correlation between Anxiety and Depression\n"
             "- Moderate correlation between Depression and Insomnia\n"
             "- Moderate correlation between Anxiety and OCD\n")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
row3_col1, row3_col2 = st.columns(2)
with row3_col1:
    st.subheader("Histograms of Different Variables")
    columns_to_plot = ["Age", "Hours per day", "BPM", "Anxiety", "Depression", "Insomnia", "OCD"]
    music[columns_to_plot].hist(bins=10, figsize=(20, 10))
    plt.suptitle("Histograms", y=0.95)
    fig_hist = plt.gcf()  # Get the current figure
    st.pyplot(fig_hist)  # Pass the figure to st.pyplot()
with row3_col2:
    st.subheader("Insights")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write(
             " - Captures more data of people between ages 15-25.\n"
             "- Most people listen to music for 1-4 hrs per day.\n"
             "- Beats per Minute usually ranges between 100-150\n"
             "- Most people in the dataset deal with Anxiety and Depression.\n")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

row4_col1, row4_col2 = st.columns(2)
with row4_col1:
    st.subheader("Primary Streaming Service")
    fig = plt.figure(figsize=(8, 4))
    sns.countplot(x=music['Primary streaming service'])
    plt.xticks(rotation=75)
    st.pyplot(fig)
with row4_col2:
    st.subheader("Insights")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("- Spotify is the most used streaming service among the participants.\n")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
row5_col1, row5_col2 = st.columns(2)
with row5_col1:
    st.subheader("Barplot - Fav genre vs Age")
    fig = plt.figure(figsize=(8, 4))
    sns.barplot(x=music['Fav genre'], y=music['Age'])
    plt.xticks(rotation=75)
    st.pyplot(fig)
with row5_col2:
    st.subheader("Insights")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("- Listeners in the age group of 35+ listen to Gospel Music more.\n"
             "- Listeners in the age group below 20 like to listen to K-pop, Rap and Latin.\n")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

row6_col1, row6_col2 = st.columns(2)
with row6_col1:
    st.subheader("Lineplots for each Mental Health problem")
    figure, axes = plt.subplots(2, 2, figsize=(18, 10))
    sns.lineplot(ax=axes[0, 0], x=music['Fav genre'], y=music['Insomnia'], ci=None)
    sns.lineplot(ax=axes[0, 1], x=music['Fav genre'], y=music['OCD'], ci=None)
    sns.lineplot(ax=axes[1, 0], x=music['Fav genre'], y=music['Depression'], ci=None)
    sns.lineplot(ax=axes[1, 1], x=music['Fav genre'], y=music['Anxiety'], ci=None)
    plt.tight_layout()
    st.pyplot(figure)
with row6_col2:
    st.subheader("Insights ")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write(" - Participants with high insomnia listen to gospel music most and country music the least.\n"
         " - Participants with high OCD listen to Lofi & Rap music the most.\n"
         " - Participants with high Depression listen to Lofi & Hip hop music the most.\n"
         " - Participants with high Anxiety listen to Folk, K-pop, Jazz, and Rock music the most.\n")
    st.write("")
    st.write("")
    st.write("")
    st.write("")


row7_col1, row7_col2 = st.columns(2)
with row7_col1:
    st.subheader("Barplots with Favourite Genre, Music Effects and Age")
    figure, axes = plt.subplots(3, 2, figsize=(20, 10))
    sns.barplot(ax=axes[0, 0], x=music['Fav genre'], y=music['Age'], hue=music['Music effects'])
    sns.barplot(ax=axes[0, 1], x=music['Fav genre'], y=music['Hours per day'], hue=music['Music effects'])
    sns.barplot(ax=axes[1, 0], x=music['Fav genre'], y=music['Insomnia'], hue=music['Music effects'])
    sns.barplot(ax=axes[1, 1], x=music['Fav genre'], y=music['OCD'], hue=music['Music effects'])
    sns.barplot(ax=axes[2, 0], x=music['Fav genre'], y=music['Depression'], hue=music['Music effects'])
    sns.barplot(ax=axes[2, 1], x=music['Fav genre'], y=music['Anxiety'], hue=music['Music effects'])
    plt.tight_layout()
    st.pyplot(figure)
with row7_col2:
    st.subheader("Insights")
    st.write(" - OCD:"
         " Lofi music is heard the most and by the age group is in mid-20s.Among the participants, Lofi music has helped improve the condition.")

    st.write(" - Insomnia:"
         " Gospel music is heard the most and in the higher age groups. Among the participants, it has helped improve the condition."
         " Rock music should be avoided by those dealing with insomnia, as it has chances of worsening the condition compared to improving."
         " Listening to Lofi and Gospel music for 4-6 hours can improve the condition.")

    st.write(" - Depression:"
         " Participants with high depression listen to Lofi and Hip Hop music the most."
         " Rock music should be avoided by those dealing with depression, as it has chances of worsening the condition compared to improving."
         " Listening to Lofi and Gospel music for 4-6 hours can improve the condition.")

    st.write(" - Anxiety:"
         " Participants with high anxiety listen to Folk, K-pop, Jazz, and Rock music the most."
         " R&B, Jazz, K-pop, Country, EDM, Hip Hop, Folk, Metal, and Latin music either have no effect or help in improving the condition but do not have any negative effects."
         " Listening to Lofi and Gospel music for 4-6 hours can improve the condition."
         " While video game music and pop, if heard for even 2 hours, showed worsening of conditions in some participants.")

