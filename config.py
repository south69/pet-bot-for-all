from dotenv import load_dotenv
import os

load_dotenv()

# Токен бота 

api_token_tg = os.getenv("API_TOKEN_TG_DEV")
# api_token_tg = os.getenv("API_TOKEN_TG_PROD")

# Подключение к БД
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# Полная строка подключения к БД
POSTGRES_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)