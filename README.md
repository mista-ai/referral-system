# Referral System API

This project is a simple RESTful API service built with Django Rest Framework (DRF) that includes user registration, authentication, and referral code management. JWT authentication is used to secure the API endpoints.

## Features

- **User Registration and Authentication:**
  - Register users with email and password.
  - Authenticate users using JWT (JSON Web Token) authentication.

- **Referral Code Management:**
  - **Create Referral Codes:** Users can generate new referral codes.
  - **Delete Referral Codes:** Users can delete their referral codes.
  - **Activate Referral Codes:** Referral codes can be activated or deactivated.
  - **Register with Referral Code:** New users can register using a referral code.


# Referral System API

## Описание

Это простой RESTful API сервис для реферальной системы, включающий регистрацию и аутентификацию пользователя, используя Django Rest Framework (DRF) и JWT аутентификацию. Сервис позволяет пользователям создавать, удалять и активировать реферальные коды, а также регистрироваться с использованием реферального кода.
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
```json
{
    "username": "testuser2",
    "password": "testpassword2",
    "email": "testuser@example2.com",
    "referral_code": "referrerusername"
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
### Создание реферального кода
#### Запрос
- Метод: POST
- URL: http://127.0.0.1:8000/api/referral/create/
- Тело запроса (JSON):
```json
{
    "code": "unique_referral_code",
    "expiration_date": "2024-12-31T23:59:59Z"
}
```
#### Ответ
- Успешный ответ (201 Created):
```json
{
    "id": 1,
    "code": "unique_referral_code",
    "expiration_date": "2024-12-31T23:59:59Z",
    "is_active": false
}
```

### Удаление реферального кода
#### Запрос
- Метод: DELETE
- URL: http://127.0.0.1:8000/api/referral/delete/
- Параметры запроса: Нет
- Требуется аутентификация
#### Ответ
- Успешный ответ (204 No Content)

### Активация реферального кода
#### Запрос
- Метод: POST
- URL: http://127.0.0.1:8000/api/referral/activate/<int:pk>/
- Параметры запроса: pk - ID реферального кода
- Требуется аутентификация
#### Ответ
- Успешный ответ (200 OK):
```json
{
    "detail": "Referral code activated successfully."
}
```
- Ответ при истекшем сроке действия (400 Bad Request):
```json
{
    "detail": "Referral code has expired."
}
```
- Ответ при неверном реферальном коде (404 Not Found):
```json
{
    "detail": "Referral code not found."
}
```

### Список реферальных кодов пользователя
#### Запрос
- Метод: GET
- URL: http://127.0.0.1:8000/api/referral/list/
- Параметры запроса: Нет
- Требуется аутентификация
#### Ответ
- Успешный ответ (200 OK):
```json
[
    {
        "id": 1,
        "code": "unique_referral_code",
        "expiration_date": "2024-12-31T23:59:59Z",
        "is_active": true
    },
    {
        "id": 2,
        "code": "another_referral_code",
        "expiration_date": "2023-12-31T23:59:59Z",
        "is_active": false
    }
]
```

