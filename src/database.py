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

def get_user_id(username):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT user_id FROM users WHERE username = %s"
            cursor.execute(query, (username,))
            row = cursor.fetchone()
            return row[0]
        except Error as e:
            st.error(f"Error getting user's word: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            conn.close()
        return False

def get_user_words(user_id):
    conn = get_connection()
    cursor = None
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT name FROM words WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            return [row[0] for row in cursor.fetchall()]
        except Error as e:
            st.error(f"Error getting user's word: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            conn.close()
    return []

def get_translation(user_id, name):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT ja_mean FROM words WHERE user_id = %s AND name = %s"
            cursor.execute(query, (user_id, name))
            result = cursor.fetchone()
            if result is not None:
                return result
        except Error as e:
            st.error(f"Error getting translation: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            conn.close()
    return None
