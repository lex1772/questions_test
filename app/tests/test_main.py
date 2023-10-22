import pytest

from fastapi.testclient import TestClient

from app.main import app, get_db
from app.models.models import Base
from app.tests.test_database import engine, TestingSessionLocal
from app.tests.test_models import Questions


# Тестовая сессия
@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()


# Тестовый клиент
@pytest.fixture()
def client(session):
    def override_get_db():
        try:

            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)


# Функция для тестирования
def test_post_questions(session, client):
    response = client.post("/10")
    assert response.status_code == 200
    assert response.json() is None
    session.add(Questions(
        question_id=12,
        question_text="abv",
        answer="gde",
        created_at="2022-12-30T22:00:31.406000",
        last_request=1
    ))
    session.commit()
    response = client.post("/10")
    assert response.status_code == 200
    assert response.json() == [
        {'answer': 'gde',
         'created_at': '2022-12-30T22:00:31.406000',
         'question_id': 12,
         'question_text': 'abv'}]
