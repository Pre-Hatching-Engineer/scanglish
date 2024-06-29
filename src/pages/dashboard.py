import streamlit as st
from database import get_user_words


def show(username):
    st.title("Dashboard")
    words = get_user_words(username)
    st.write(f"Total words learned: {len(words)}")
    st.write("Recent words:")
    for word in words[-5:]:
        st.write(word)
