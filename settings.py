import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(".env")


class DBSettings:
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DB_CHUNK_SIZE = os.getenv("DB_CHUNK_SIZE")
