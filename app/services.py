import json

import requests
from pydantic import PositiveInt
from sqlalchemy.orm import Session
from sqlalchemy.util import deprecations

from app.models.models import Questions

# Отмена предупреждений при тестировании в pytest
deprecations.SILENCE_UBER_WARNING = True


# Получение вопросов
def get_questions(num):
    response = requests.get(f'https://jservice.io/api/random?count={num}')
    parsed = json.loads(response.content)
    return parsed


# Получение вопросов из БД с ограничением на последний запрос
def get_from_db(db, last_request):
    return db.query(Questions.question_id,
                    Questions.question_text,
                    Questions.answer,
                    Questions.created_at).order_by(
        Questions.id.desc()
    ).limit(last_request.last_request)


# Создание вопросов в БД с возвратом последнего запроса
def create_questions(db: Session, num: PositiveInt):
    counter = num
    first_question = db.query(Questions).order_by(Questions.id.desc()).first()
    if first_question is None:
        last_question = None
    else:
        last_question = get_from_db(db=db, last_request=first_question).all()
    while counter > 0:
        questions = get_questions(counter)
        for question in questions:
            question_id = question.get('id')
            if db.query(Questions).get(question_id) is None:
                question_text = question.get('question')
                answer = question.get('answer')
                created_at = question.get('created_at')
                db_question = Questions(
                    question_id=question_id,
                    question_text=question_text,
                    answer=answer,
                    created_at=created_at,
                    last_request=num
                )
                db.add(db_question)
                db.commit()
                db.refresh(db_question)
                counter -= 1
            else:
                counter -= 0
    return last_question
