# import io
# import sys

# import pytesseract
# import streamlit as st
# from PIL import Image


# # データベース接続
# def extract_words(image):
#     text = pytesseract.image_to_string(image, lang="jpn+eng")
#     words = text.split()
#     return words


# # pytesseactを使ってテキスト抽出
# def image_to_text(image):
#     # 画像を読み込む
#     img = Image.open(image)
#     # TesseractでOCRを実行
#     text = pytesseract.image_to_string(img, lang="jpn")
#     return text


# st.title("Scan your image")

# # サイドバーナビゲーション
# page = st.sidebar.radio("", ["画像読み込み", "単語帳", "文章生成"])

# # 2列のカラムを作成
# col1, col2 = st.columns(2)

# # col1にアップロード機能を表示
# with col1:
#     st.header("Upload Image")
#     uploaded_file = st.file_uploader("画像をアップロード", type=["png", "jpg", "jpeg"])

# # col2にテキストを表示
# with col2:
#     st.header("Extracted Text")
#     if uploaded_file is not None:
#         text = image_to_text(uploaded_file)
#         st.write(text)
#         words = extract_words(uploaded_file)
