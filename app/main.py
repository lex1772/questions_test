from fastapi import FastAPI, Depends
from pydantic import PositiveInt
from sqlalchemy.orm import Session

from app.db import LocalSession
from app.services import create_questions

# Основная точка взаимодействия для создания всего API
app = FastAPI()


# Зависимость базы данных для создания
# сеанса базы данных и закрытия его после завершения.
def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()


# Путь с методом post, в который пользователь передает
# количество вопросов и получает последний запрос
@app.post("/{questions_num}")
def post_questions_num(
        questions_num: PositiveInt, db: Session = Depends(get_db)
):
    return create_questions(num=questions_num, db=db)
