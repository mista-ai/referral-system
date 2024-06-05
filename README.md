# Referral System API

## Описание

Это простой RESTful API сервис для реферальной системы, включающий регистрацию и аутентификацию пользователя, используя Django Rest Framework (DRF), JWT аутентификацию и Google OAuth 2.0.

## Использование

### Регистрация пользователя

#### Запрос

- Метод: POST
- URL: `http://127.0.0.1:8000/api/register/`
- Тело запроса (JSON):

```json
{
    "username": "testuser",
    "password": "testpassword",
    "email": "testuser@example.com"
}
```
#### Ответ
- Успешный ответ (201 Created):
### Вход пользователя
#### Запрос
- Метод: POST
- URL: http://127.0.0.1:8000/api/login/
- Тело запроса (JSON):

```json
{
    "username": "testuser",
    "password": "testpassword"
}
```
#### Ответ
- Успешный ответ (200 OK):
```json
{
    "refresh": "<YOUR_REFRESH_TOKEN>",
    "access": "<YOUR_ACCESS_TOKEN>"
}
```
### Обновление токена
#### Запрос
- Метод: POST
- URL: http://127.0.0.1:8000/api/token/refresh/
- Тело запроса (JSON):
```json
{
    "refresh": "<YOUR_REFRESH_TOKEN>"
}
```
#### Ответ
- Успешный ответ (200 OK):
```json
{
    "access": "<NEW_ACCESS_TOKEN>"
}
```
