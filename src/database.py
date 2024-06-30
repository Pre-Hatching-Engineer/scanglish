import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime

# configのインポート
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD


def get_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            charset="utf8mb4",
            collation="utf8mb4_general_ci",
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


def getWordsList(user_id, num_words):
    conn = get_connection()
    cursor = None
    if conn:
        try:
            cursor = conn.cursor()
            # num_wordsの数だけランダムに単語を取得する, 現在のユーザーの単語帳のみを取得する
            query = "SELECT word_name FROM words WHERE user_id = %s ORDER BY RAND() LIMIT %s"
            cursor.execute(query, (user_id, num_words))
            # 単語のリストを返す
            return [row[0] for row in cursor.fetchall()]
        except Error as e:
            st.error(f"Error getting words list: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            conn.close()
    return []


def get_user_id(username):
    conn = get_connection()
    cursor = None
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT user_id FROM users WHERE username = %s"
            cursor.execute(query, (username,))
            user_id = cursor.fetchone()[0]
            cursor.fetchall()
            return user_id
        except Error as e:
            st.error(f"Error getting user id: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            conn.close()
    return None


def add_word(words_list, translated_list, user_id):
    conn = get_connection()
    cursor = None
    if conn:
        try:
            # usernameからuser_idを取得する
            cursor = conn.cursor()
            # 単語と翻訳をwordsテーブルに追加する
            for word, word_ja in zip(words_list, translated_list):
                query = "INSERT INTO words (user_id, word_name, ja_mean) VALUES (%s, %s, %s)"
                cursor.execute(query, (user_id, word, word_ja))
            conn.commit()
        except Error as e:
            st.error(f"Error adding word: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            conn.close()


def show_jawords_list():
    conn = get_connection()
    cursor = None
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT word_name, ja_mean FROM words"
            cursor.execute(query)
            words_list = cursor.fetchall()
            return words_list
        except Error as e:
            st.error(f"Error getting words list: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            conn.close()
    return []
