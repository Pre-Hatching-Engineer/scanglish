import sqlite3
import streamlit as st


def init_db():
    conn = sqlite3.connect("english_learning.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS words
                 (username TEXT, word TEXT)"""
    )
    conn.commit()
    conn.close()


@st.cache_resource
def get_connection():
    return sqlite3.connect("english_learning.db", check_same_thread=False)


def add_word(username, word):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO words VALUES (?, ?)", (username, word))
    conn.commit()


def get_user_words(username):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT word FROM words WHERE username = ?", (username,))
    return [row[0] for row in c.fetchall()]
