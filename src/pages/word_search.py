import streamlit as st
from database import get_user_words


def show(username):
    st.title("Word Search")
    search = st.text_input("Search for a word:")
    if st.button("Search"):
        words = get_user_words(username)
        if search in words:
            st.success(f"'{search}' is in your word list!")
        else:
            st.error(f"'{search}' is not in your word list.")
