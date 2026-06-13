# Блог — Посты (Django)

Веб-приложение для управления постами в блоге. Экзаменационный билет, вариант 2.

## Требования

- Python 3.10+
- Django 5+

## Установка

```bash
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

Приложение будет доступно по адресу http://127.0.0.1:8000/

## Функциональность

- CRUD для постов (список, создание, редактирование, удаление с подтверждением)
- Серверная валидация данных
- Кастомная страница 404
- Middleware для подсчёта запросов и кодов ответа (консоль + `metrics.log`)
- Настройки через `.env`
- Статические файлы через WhiteNoise (работает при `DEBUG=False`)
- Интеграционный тест главной страницы

## Тесты

```bash
python manage.py test
```

## Сбор статики (для production)

```bash
python manage.py collectstatic --noinput
```
