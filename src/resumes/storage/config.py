import psycopg2
from typing import NamedTuple

import os
from dotenv import load_dotenv

loaded_env = load_dotenv(".env")
if not loaded_env:
    exit("Не найден .env файл!")


class Settings(NamedTuple):
    Database: str
    User: str
    Password: str
    Host: str
    Port: str
    

settings = Settings(
    Database=os.getenv("RESUME_POSTGRES_DB"),
    User=os.getenv("RESUME_POSTGRES_USER"),
    Password=os.getenv("RESUME_POSTGRES_PASSWORD"),
    Host=os.getenv("RESUME_POSTGRES_HOST"),
    Port=os.getenv("RESUME_POSTGRES_PORT"),
)

TABLE_CITY = "city"
TABLE_RESUME = "resume"
TABLE_EDUCATION = "education"
TABLE_ADDITIONAL = "additional"
TABLE_POSITION = "position"
TABLE_EXPERIENCE_STEP = "experience_step"
    
def connect() -> psycopg2.extensions.connection:
    try:
        db = psycopg2.connect(
            database=settings.Database,
            user=settings.User,
            password=settings.Password,
            host=settings.Host,
            port=int(settings.Port),
        )
        return db
    except BaseException as err:
        exit(f"Не удалось подключиться к БД: {err}")