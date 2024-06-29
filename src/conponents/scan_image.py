import streamlit as st


def scanImage():
    # ログインしてなければ何も表示しない
    if st.session_state.username is None:
        return
    st.title("Scan Image")
    st.write("Coming soon!")
