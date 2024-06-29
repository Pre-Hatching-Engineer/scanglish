import streamlit as st
import io
import re
import sys
import pytesseract
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


def text_cleaning(text):
    # textをすべて小文字に変換
    text = text.lower()
    # textから記号を削除
    text = re.sub(r"[^\w\s]|[\d]", "", text)
    # 空白ごとにsetに変換し、重複を削除
    words = set(text.split())
    return words


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
            words = text_cleaning(text)
            print(words)
            print(type(words))
            words_list = list(words)
            st.write(words_list)
            print(type(words_list))


if __name__ == "__main__":
    scanImage()
