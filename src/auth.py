import streamlit as st
import hashlib
from database import add_user, check_user


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def authenticate():
    st.title("Login")
    choice = st.radio("sign up or login", ("Sign up", "Login"))

    if choice == "Login":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if check_user(username, hash_password(password)):
                st.session_state.username = username
                st.success("Logged in successfully!")
            else:
                st.error("Incorrect username or password.")
    elif choice == "Sign up":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Sign up"):
            add_user(username, hash_password(password))
            st.success("User added successfully!")
