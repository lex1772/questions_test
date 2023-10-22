# Сервис для получения вопросов с https://jservice.io
Простое REST API приложение, которое принимает на вход POST запрос с количеством вопросов и отдает последний предыдущий сохраненный запрос викторины

:white_check_mark: Реализовано REST API, принимающее на вход POST запросы с содержимым вида {"questions_num": integer}.

:white_check_mark: База данных запускается как Docker контейнер.

:white_check_mark: Проект запускается через Docker-compose.

:white_check_mark: Написаны тесты.

Стек технологий:

- FastAPI
- PostgreSQL
- Flake8
- Pytest
- python-dotenv
- requests
- SQLAlchemy
- pydantic

### Начало работы
1. Заполнить .env файл в соответствии с .env_sample
2. Создать образ с помощью команды `docker-compose build`
3. Запустить контейнеры с помощью команды `docker-compose up`
4. Открыть postman и в workspace вставить в строку адрес c POST запросом `http://localhost:8000/{question_num}`
5. (Необязательно) При наборе команды pytest запустится тестирование

### Примеры запросов к API
POST /password/2 - Получаем в ответ None, так как прошлого запроса не было
POST /password/2 - Получаем в ответ список из двух вопросов, так как прошлый запрос был на 2 вопроса
![Пример запроса](https://github.com/lex1772/questions_test/assets/123934765/cc8fdbf9-b0b4-457d-815c-4623ef2d746d)
