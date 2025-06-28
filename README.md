## MINI-TRELLO

This is an API project called MINI-TRELLO built with Django Rest Framework.

## How to run the Project locally

- Install Python
- Git clone the project with `https://github.com/Aderinmola/mini-trello.git`
- change directory with `cd mini-trello`
- Create your virtualenv with `py -m venv venv` and activate it.
- Install the requirements with `pip install -r requirements.txt`
- Finally run the API, in another terminal
  `python manage.py runserver`
- Go ahead to test the endpoints listed in the table below with postman, using the base url ` http://127.0.0.1:8000/swagger/`

### 📬 Deployed Link

`https://mini-trello-voyp.onrender.com/swagger/`

## ROUTES TO IMPLEMENTED

| METHOD   | ROUTE               | FUNCTIONALITY       | ACCESS          |
| -------- | ------------------- | ------------------- | --------------- |
| _User_   |
| _GET_    | `/user/register/`   | _Create a User_     | _Register user_ |
| _POST_   | `/login/`           | _Login a User_      | _Login user_    |
| _POST_   | `/user/profile/`    | _View User Profile_ | _View Profile_  |
| _Board_   |
| _GET_    | `/boards/`      | _Get all Board_      | _Get Boards_     |
| _POST_   | `/boards/`      | _Create a Board_     | _Create Board_   |
| _GET_    | `/boards/{id}/` | _Get a Board_        | _Get Board_      |
| _PUT_    | `/boards/{id}/` | _Update a Board_     | _Update Board_   |
| _DELETE_ | `/boards/{id}/` | _Delete a Board_     | _Delete Board_   |
| _Task_   |
| _GET_    | `/task/`      | _Get all Task_      | _Get Tasks_     |
| _POST_   | `/task/`      | _Create a Task_     | _Create Task_   |
| _GET_    | `/task/{id}/` | _Get a Task_        | _Get Task_      |
| _PUT_    | `/task/{id}/` | _Update a Task_     | _Update Task_   |
| _DELETE_ | `/task/{id}/` | _Delete a Task_     | _Delete Task_   |
