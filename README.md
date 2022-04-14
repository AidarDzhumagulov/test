# Сервер на FastAPI

## Для запуска
- Склонировать репозиторий командой `git clone`
- Запуск docker-compose командой `docker-compose up`

## Для CRUD действий в Swagger
- Зайти на локалхост, порт 8000
- Добавить **/docs** к локалхосту. Будет примерно так: **localhost:8000/docs**
- Выполнить действия и наслаждаться этим

## Для доступа в БД
- В **docker-compose** создан образ **adminer**
- При запуске **docker-compose** переходите по сылке **adminer** и можете видеть за своими изменениями в БД

## Для локального запуска
- Склонировать репозиторий командой `git clone`
- Создать виртуальное окружение и устновить зависимости
Команды:
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```
- Далее запуск идет через Uvicorn `uvicorn app/main:app --reload`