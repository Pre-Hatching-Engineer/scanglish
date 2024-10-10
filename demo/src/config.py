import os
from dotenv import load_dotenv

load_dotenv()

# データベース設定
DB_NAME = os.getenv("MYSQL_DATABASE", "")
DB_HOST = os.getenv("MYSQL_HOST", "localhost")
DB_USER = os.getenv("MYSQL_USER", "")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD", "")

# OpenAI API設定
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
