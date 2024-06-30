import streamlit as st
import mysql.connector
from mysql.connector import Error

# configのインポート
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD


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
    if conn:
        try:
            cursor = conn.cursor()
            # query = f"insert into users (username, password_hash) values ('{username}', '{password_hash}')"
            # cursor.execute(query)
            query = "INSERT INTO users (username, password_hash) VALUES (%s, %s)"  # 修正箇所
            cursor.execute(query, (username, password_hash))  # 修正箇所
            conn.commit()
        except Error as e:
            st.error(f"Error adding user: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            conn.close()


def check_user(username, password_hash):
    conn = get_connection()
    cursor = None
    if conn:
        try:
            cursor = conn.cursor()
            # query = f"select * from users where username = '{username}' and password_hash = '{password_hash}'"
            # cursor.execute(query)
            query = "SELECT * FROM users WHERE username = %s AND password_hash = %s"  # 修正箇所
            cursor.execute(query, (username, password_hash))  # 修正箇所
            return cursor.fetchone() is not None
        except Error as e:
            st.error(f"Error checking user: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            conn.close()
    return False


def add_word(username, words_list, translated_list):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            # useridを取得
            query = "INSERT INTO words (user_id, n) VALUES (%s, %s, %s)"
            for word, translation in zip(words_list, translated_list):
                cursor.execute(query, (username, word, translation))
            conn.commit()
        except Error as e:
            st.error(f"Error adding word: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            conn.close()


def get_user_words(username):
    # conn = get_connection()
    # c = conn.cursor()
    # c.execute("SELECT word FROM words WHERE username = ?", (username,))
    # return [row[0] for row in c.fetchall()]
    pass
