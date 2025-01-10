import streamlit as st

st.title("Learning Streamlit")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")

st.header("My First App!")

st.write("Learning Streamlit for the first time.")

agree = st.checkbox("I agree with Parina.")

if agree:
    st.write("Great!")

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
elif genre == "***Drama***":
    st.write("Who doesn't love drama... Hahahah")
else:
    st.write("You seriously like watching documentary.. are you kidding me?")