## MINI-TRELLO

This is an API project called TASK-MANAGER built with Django Rest Framework.

## How to run the Project locally

- Install Python
- Git clone the project with `https://github.com/Aderinmola/taskmanager.git`
- change directory with `cd taskmanager`
- Create your virtualenv with `py -m venv venv` and activate it.
- Install the requirements with `pip install -r requirements.txt`
- Finally run the API, in another terminal
  `python manage.py runserver`
- Go ahead to test the endpoints listed in the table below with postman, using the base url ` http://127.0.0.1:8000/swagger/`

### 📬 Deployed Link

`https://taskmanager-v12r.onrender.com/swagger/`

## ROUTES TO IMPLEMENTED

| METHOD   | ROUTE               | FUNCTIONALITY       | ACCESS          |
| -------- | ------------------- | ------------------- | --------------- |
| _User_   |
| _GET_    | `/register/`   | _Create a User_     | _Register user_ |
| _POST_   | `/login/`           | _Login a User_      | _Login user_    |
| _POST_   | `/profile/`    | _View User Profile_ | _View Profile_  |
| _Task_   |
| _GET_    | `/tasks/`      | _Get all Task_      | _Get Tasks_     |
| _POST_   | `/tasks/`      | _Create a Task_     | _Create Task_   |
| _GET_    | `/tasks/{id}/` | _Get a Task_        | _Get Task_      |
| _PUT_    | `/tasks/{id}/` | _Update a Task_     | _Update Task_   |
| _DELETE_ | `/tasks/{id}/` | _Delete a Task_     | _Delete Task_   |
| _PATCH_ | `/tasks/{id}/task_completed/` | _Patch a Task_     | _Patch Task_   |

