import io
import re
import sys
import os
import requests
from database import add_word, get_user_id, show_jawords_list
import pytesseract
import streamlit as st
import streamlit as st
from PIL import Image


def extract_words(image):
    text = pytesseract.image_to_string(image, lang="jpn+eng")
    words = text.split()
    return words


# pytesseactを使ってテキスト抽出
def image_to_text(image):
    # 画像を読み込む
    img = Image.open(image)
    # TesseractでOCRを実行
    text = pytesseract.image_to_string(img, lang="jpn")
    return text


def load_stopwords():
    with open("src/components/stopwords.txt", "r") as file:
        stopwords = set(line.strip() for line in file)
    return stopwords


def text_cleaning(text, stopwords):
    # textをすべて小文字に変換
    text = text.lower()
    # アルファベットとスペース以外の文字を削除
    text = re.sub(r"[^a-z ]", "", text)
    # スペースを改行に変換
    text = text.replace(" ", "\n")
    # 改行ごとに分割し、空の要素を除外し、重複を削除
    words = set(word for word in text.split("\n") if word)
    # stopwordsを除外
    cleaned_words = [word for word in words if word not in stopwords]
    return cleaned_words


def get_translation(words_list):
    # 翻訳後のリストを取得する
    translated_list = []
    target_lang = "JA"
    DEEPL_API_KEY = "9aa834ef-c010-4c82-9975-e25ba7f23744:fx"  # APIキーを設定
    text_to_translate = "\n".join(words_list)  # 単語を改行で区切って一度に翻訳
    params = {"auth_key": DEEPL_API_KEY, "text": text_to_translate, "target_lang": target_lang}
    response = requests.post("https://api-free.deepl.com/v2/translate", data=params)
    if response.status_code == 200:
        translated_texts = response.json()["translations"][0]["text"].split("\n")
        translated_list.extend(translated_texts)
    else:
        st.write("Failed to translate")
        translated_list = [None] * len(words_list)  # 翻訳に失敗した場合はNoneを追加

    return translated_list


def scanImage():
    st.title("Scan your image")

    # 2列のカラムを作成
    col1, col2 = st.columns(2)

    # col1にアップロード機能を表示
    with col1:
        st.header("Upload Image")
        uploaded_file = st.file_uploader("画像をアップロード", type=["png", "jpg", "jpeg"])
        if uploaded_file is not None:
            # アップロードされた画像を表示
            st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

    # col2にテキストを表示
    with col2:
        st.header("Extracted Text")
        if uploaded_file is not None:
            text = image_to_text(uploaded_file)
            st.write(text)
            stopwords = load_stopwords()
            words = text_cleaning(text, stopwords)
            words_list = list(words)
            st.write(words_list)
            translated_list = get_translation(words_list)
            st.write(translated_list)
            user_id = get_user_id(st.session_state.username)
            add_word(words_list, translated_list, user_id)
            # テスト
            # result = show_jawords_list()
            # print(result)


if __name__ == "__main__":
    scanImage()
