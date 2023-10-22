import os

from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Загрузка .env файла
load_dotenv(find_dotenv())

# Соединение с базой данных
db_url = (f'postgresql://{os.getenv("DB_USER")}:'
          f'{os.getenv("DB_PASSWORD")}'
          f'@db:5432/{os.getenv("DB_NAME")}')

# Инициализируем движок БД
engine = create_engine(db_url)

# Создание сессии
LocalSession = sessionmaker(bind=engine)
