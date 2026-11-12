import os

import streamlit as st
from google import genai
from dotenv import load_dotenv
import time
load_dotenv()
GEMINI_API_KEY= os.getenv("GEMINI_API_KEY")
client = genai.Client()
st.set_page_config(
    page_title="janvi's App",
    page_icon="📊",  # Optional: emoji or image path
    layout="wide"    # Optional: layout configuration
)
st.title("✈️Travel Assistant Friend🚇")
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        -45deg,
        #DFF6FF,
        #BDEBFF,
        #A5DDF5,
        #EAFBFF,
        #C5EFFF
    );
    background-size: 400% 400%;
    animation: oceanMove 12s ease infinite;
}

@keyframes oceanMove {
    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}
.stApp h1,
.stApp h2,
.stApp h3 {
    color: #123B50;
    font-weight: 800;
}

.stApp p {
    color: #24566B;
}

.stApp label {
    color: #123B50;
    font-weight: 600;
}
/* Main text colour */
.stApp,
.stApp p,
.stApp span,
.stApp label,
.stApp h1,
.stApp h2,
.stApp h3,
.stMarkdown,
.stCaption {
    color: #123B50 !important;
}

/* Input labels */
.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stRadio label {
    color: #123B50 !important;
}

/* Radio button text */
.stRadio div[role="radiogroup"] label {
    color: #24566B !important;
}

/* Select box text */
.stSelectbox div[data-baseweb="select"] {
    color: #123B50 !important;
}

/* Button text */
.stButton button {
    color: #FFFFFF !important;
}
/* Text displayed using st.write() */
.stApp [data-testid="stMarkdownContainer"] p,
.stApp [data-testid="stMarkdownContainer"] li,
.stApp [data-testid="stMarkdownContainer"] strong,
.stApp [data-testid="stMarkdownContainer"] em {
    color: #123B50 !important;
}

/* General Streamlit text */
.stApp [data-testid="stText"],
.stApp .stMarkdown {
    color: #123B50 !important;
}
</style>
""", unsafe_allow_html=True)

st.caption("Your friendly travel buddy, always ready to turn "
    "your travel dreams into unforgettable adventures! 🌎💙")

Destination = st.text_input("Enter Your Destination Buddy: ")
Days = st.number_input("Enter Number Of Days Buddy:",min_value=1,max_value = 30)
budget = st.selectbox("select your budget",["select your travel type","luxury","Moderate","Budgeted"])
Travel_type = st.radio("who are you traveling with?",["Family","Friends","solo"])
prompt = f"""you are an experienced travel agent.you are helping the user to{Destination} plan a trip for {Days}in a very friendly way in a bullet form you will answer the user using some gen z slangs if needed but very few of it ,he or she is travelling with{Travel_type} with abudget of {budget} and you will give the user a detailed plan for the trip with some tips and tricks to make the trip more enjoyable and memorable"""

st.button("Let's Plan My Trip! ✈️")
interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=prompt
   )

with st.spinner("Triangulating..."):
    time.sleep(5)  # Simulate a delay for the spinner

st.markdown(
    """
    <p style="
        color: #0077B6;
        font-size: 22px;
        font-weight: bold;
        text-align: center;
    ">
        Yay! Let's plan an amazing adventure together! 🌍
    </p>
    """,
    unsafe_allow_html=True
)
#st.success("Yay! Let's plan an amazing adventure together! 🌍")
st.write("Enjoy Your Trip to", Destination,"for",Days,"days buddy! 🏖️✈️")

st.balloons()
st.write("Here's Your Plan Ready To Go buddy! Replies: \n\n", interaction.output_text)