from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base

from app.db import engine

# Базовый класс SQLAlchemy
Base = declarative_base()


# Модель вопросов для работы с БД и SQLAlchemy
class Questions(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    question_id = Column(Integer, unique=True)
    question_text = Column(String)
    answer = Column(String)
    created_at = Column(DateTime)
    last_request = Column(Integer)

    def __repr__(self):
        return f"<id(id={self.id}, " \
               f"question_text=\"{self.question_text}\", " \
               f"answer=\"{self.answer}\", " \
               f"created_at={self.created_at})>"

    def __str__(self):
        return f'{self.question_text}'


# Создание таблицы вопросов, если она не существует
try:
    Questions.__table__.create(engine)
except Exception:
    pass
