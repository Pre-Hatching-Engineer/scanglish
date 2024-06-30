import streamlit as st

# セッションの初期化
if "username" not in st.session_state:
    st.session_state.username = None
from auth import authenticate
from components import word_search, generate_sentence, scan_image
from st_on_hover_tabs import on_hover_tabs


def main():
    st.set_page_config(layout="wide", page_title="Scanglish", page_icon="🔍")

    if st.session_state.username is None:
        authenticate()
    else:
        # page = st.sidebar.radio("", ["画像スキャン", "単語帳", "文章生成"])
        # if st.sidebar.button("画像スキャン"):
        #     word_search()
        st.markdown("<style>" + open("static/style.css").read() + "</style>", unsafe_allow_html=True)

        with st.sidebar:
            tabs = on_hover_tabs(
                tabName=["画像読み込み", "単語帳", "文章生成"],
                iconName=["📸", "📚", "📝"],
                default_choice=0,
            )

        if tabs == "画像読み込み":
            scan_image.scanImage()
        elif tabs == "単語帳":
            word_search.wordSearch()
        elif tabs == "文章生成":
            generate_sentence.generateSentence()
        st.sidebar.markdown(f"<h1 style='color: white;'>Welcome, {st.session_state['username']}!</h1>", unsafe_allow_html=True)
        st.sidebar.button("Logout", on_click=logout)


def logout():
    st.session_state.username = None


if __name__ == "__main__":
    main()
