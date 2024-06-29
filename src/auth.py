import streamlit as st
import hashlib


def authenticate():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if check_credentials(username, password):
            st.session_state.username = username
            st.success("Logged in successfully!")
        else:
            st.error("Incorrect username or password")


def check_credentials(username, password):
    # 実際のアプリケーションではデータベースでチェックします
    # これはデモ用の簡単な実装です
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return username == "demo" and hashed_password == hashlib.sha256("password".encode()).hexdigest()
