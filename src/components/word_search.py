import streamlit as st
from database import get_user_words


def wordSearch():
    if st.session_state.username is None:
        return
    st.title("Word Search")
    search = st.text_input("Search for a word:")
    if st.button("Search"):
        words = get_user_words(st.session_state.username)
        if search in words:
            st.success(f"'{search}' is in your word list!")
        else:
            st.error(f"'{search}' is not in your word list.")


if __name__ == "__main__":
    wordSearch()
