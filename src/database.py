import streamlit as st
import mysql.connector
from mysql.connector import Error

# configのインポート
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD


@st.cache_resource
def get_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        return conn
    except Error as e:
        st.error(f"Error connecting to MySQL: {e}")
        return None


def add_user(username, password_hash):
    conn = get_connection()
    cursor = None
    if conn:
        try:
            cursor = conn.cursor()
            query = f"insert into users (username, password_hash) values ('{username}', '{password_hash}')"
            cursor.execute(query)
            conn.commit()
        except Error as e:
            st.error(f"Error adding user: {e}")
        finally:
            cursor.close()
            conn.close()


def check_user(username, password_hash):
    conn = get_connection()
    cursor = None
    if conn:
        try:
            cursor = conn.cursor()
            query = f"select * from users where username = '{username}' and password_hash = '{password_hash}'"
            cursor.execute(query)
            return cursor.fetchone() is not None
        except Error as e:
            st.error(f"Error checking user: {e}")
        finally:
            cursor.close()
            conn.close()
    return False


def add_word(username, word):
    # conn = get_connection()
    # c = conn.cursor()
    # c.execute("INSERT INTO words VALUES (?, ?)", (username, word))
    # conn.commit()
    pass


def get_user_words(username):
    # conn = get_connection()
    # c = conn.cursor()
    # c.execute("SELECT word FROM words WHERE username = ?", (username,))
    # return [row[0] for row in c.fetchall()]
    pass
