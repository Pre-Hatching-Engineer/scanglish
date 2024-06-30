import streamlit as st
import pandas as pd
from database import get_translation
from functools import partial

def clearText():
    st.session_state.text_input = ""

def searchText(words):
    if st.session_state.text_input in words:
        st.session_state.text_output = st.session_state.text_input
    else:
        st.error(f"'{st.session_state.text_input}' is not in your word list.")

def wordSearch():
    if st.session_state.username is None:
        return
    
    st.title("Word Search")

    left, right = st.columns(2)
    # 検索単語入力部
    with left:
        # 入力部のセッションステートの初期化
        if 'text_input' not in st.session_state:
            st.session_state.text_input = ""
        # 検索結果のセッションステートの初期化
        if 'text_output' not in st.session_state:
            st.session_state.text_output = ""

        # テキスト入力
        st.text_input("Search for a word:", value=st.session_state.text_input, key="text_input")

        # wordsはデータベースからリストとして取得
        #words = get_user_words(st.session_state.username)
        words = ["happy", "angry", "sad", "pleased"] # サンプル．データベースからの返り値はレコード単位なので要修正
        trans = ["幸せな", "怒った", "悲しい", "嬉しい"]

        st.button("Search", on_click=partial(searchText, words))
        st.button("Clear", on_click=clearText)

    # 検索結果表示部
    with right:
        # st.text_area("", height=300, value=st.session_state.text_output)
        input_dict = {
            '単語': [],
            '訳': []
        }
        df = pd.DataFrame.from_dict(input_dict)
        st.dataframe(df, use_container_width=True)

if __name__ == "__main__":
    wordSearch()
