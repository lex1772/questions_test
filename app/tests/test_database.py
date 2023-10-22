import os

from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

# Загрузка .env файла
load_dotenv(find_dotenv())

# Настройки тестовой базы данных
test_db_url = (f'postgresql://{os.getenv("DB_USER")}:'
               f'{os.getenv("DB_PASSWORD")}'
               f'@localhost:5432/test_db')

# Движок тестовой базы данных
engine = create_engine(test_db_url)

# Сессия тестовой базы данных
TestingSessionLocal = (
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

# Создание тестовой базы данных
if not database_exists(engine.url):
    create_database(engine.url)
