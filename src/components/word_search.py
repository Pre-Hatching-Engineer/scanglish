import streamlit as st
import pandas as pd
from database import get_user_id,get_user_words,get_translation
from functools import partial


def clearText():
    st.session_state.text_input = ""

def searchText(user_id):
    # wordsはデータベースからリストとして取得
    words = get_user_words(user_id)
    if st.session_state.text_input in words:
        st.session_state.text_output = st.session_state.text_input
        st.session_state.trans = get_translation(user_id, st.session_state.text_output)
        if st.session_state.trans is None:
            st.session_state.trans = ""
    else:
        st.error(f"'{st.session_state.text_input}' is not in your word list.")

def wordSearch():

    if st.session_state.username is None:
        return
    else:
        user_id = get_user_id(st.session_state.username)

    # 入力部のセッションステートの初期化
    if 'text_input' not in st.session_state:
        st.session_state.text_input = ""
    # 検索結果のセッションステートの初期化
    if 'text_output' not in st.session_state:
        st.session_state.text_output = ""
    if 'trans' not in st.session_state:
        st.session_state.trans = ""
    
    st.title("Word Search")

    left, right = st.columns(2)
    # 検索単語入力部
    with left:
        # テキスト入力
        st.text_input("Search for a word:", value=st.session_state.text_input, key="text_input")

        st.button("Search", on_click=partial(searchText, user_id))
        st.button("Clear", on_click=clearText)

    # 検索結果表示部
    with right:
        # st.text_area("", height=300, value=st.session_state.text_output)
        input_dict = {
            '単語': [st.session_state.text_output],
            '訳': [st.session_state.trans]
        }
        df = pd.DataFrame.from_dict(input_dict)
        st.dataframe(df, use_container_width=True)

if __name__ == "__main__":
    wordSearch()
