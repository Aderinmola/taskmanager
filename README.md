## JWT-AUTH

This is an API project called JWT-AUTH built with Django.

## How to run the Project locally

- Install Python
- Git clone the project with `https://github.com/Aderinmola/jwt-auth.git`
- change directory with `cd jwt-auth`
- Create your virtualenv with `py -m venv venv` and activate it.
- Install the requirements with `pip install -r requirements.txt`
- Finally run the API, in another terminal
  `python manage.py runserver`
- Go ahead to test the endpoints listed in the table below with postman, using the base url ` http://127.0.0.1:8000/swagger/`

### 📬 Deployed Link

`https://jwt-auth-uqcu.onrender.com/swagger/`

## ROUTES TO IMPLEMENTED

| METHOD  | ROUTE             | FUNCTIONALITY       | ACCESS          |
| ------- | ----------------- | ------------------- | --------------- |
| _Quote_ |
| _GET_   | `/user/register/` | _Create a User_     | _Register user_ |
| _POST_  | `/token/`         | _Login a User_      | _Login user_    |
| _POST_  | `/user/profile/`  | _View User Profile_ | _View Profile_  |
