import streamlit as st


def generateSentence():
    # ログインしてなければ何も表示しない
    if st.session_state.username is None:
        return
    st.title("Generate Sentence")
    st.write("Coming soon!")


if __name__ == "__main__":
    generateSentence()
