import os
from dotenv import load_dotenv

load_dotenv()

# データベース設定
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "english_learning")

# OpenAI API設定
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
