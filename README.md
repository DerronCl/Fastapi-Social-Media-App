# Fastapi-Social-Media-App
A complex social media app that runs on the FastApi. In a nutshell, the app allows users to sign and communicate with one another by creating and editing posts. All the posts are saved to a PostgreSQL database which can be seen by other users. The app uses pydantic models and schemas to structure how messages are sent over the network like a standard social media app. Oauth2 security is used for password login and token verification. I used the Postman API client to test and debug the app while in development. You can also use Fastapi'Swagger UI as a substituite 

# Set up Instructions
1. First, create a folder named Fastapi. Then create a vritual enviroment and use pip install to download all the packages in the requirements.txt file. Use the following folder structure to prevent import errors:
                      FastAPI/
                      │
                      ├── Project/
                      │   ├── __init__.py
                      │   ├── auth2.py
                      │   └── database.py
                      │   └── main.py
                      │   └── models.py
                      │   └── schemas.py
                      │   └── utils.py
                      │   └── Router/
                      |       └── auth.py
                      |       └── post.py
                      |       └── user.py
                      ├── tests/
                      │   ├── tests.py
                      │ 
                      ├── requirements.txt

2. Next, go to the fastapi tutorial website and follow the instructions on how to set up your fastapi. Here's the link: https://fastapi.tiangolo.com/tutorial/
3. You have to reload app every time you want to use it. After the intial reload, Fastapi will automically save any changes and keep the app running continously.
Here's example code of app reload: 

  uvicorn main:app --reload
  INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
  INFO:     Started reloader process [28720]
  INFO:     Started server process [28722]
  INFO:     Waiting for application startup.
  INFO:     Application startup complete.

The command uvicorn main:app refers to:
    main: the file main.py (the Python "module").
    app: the object created inside of main.py with the line app = FastAPI().
    --reload: make the server restart after code changes. Only use for development.

4. Follow the Fastapi tutorial on how to setup CRUD path operations and decorators to famailairze yourself with the language. The tutorial will serve as an amazing reference to understanding the structure of the app. 
5. Make sure to import pydantic to establish the declaritive models and schemas for sending data over the API. 
6. Lastly, download PostgreSQL and create an account with a password. Create a Fastapi database with the required tables to store data. Using the psycopg2 modue, connect to Postgres Database. Postgres must be running for the app to connect to the database. 
7. Follow the Fastapi tutorial to understand OAuth2 with Password (and hashing) and Bearer with JWT tokens.

Here's the link to the original project on youtube: https://www.youtube.com/watch?v=0sOvCWFmrtA&t=29879s

# App Functions and Files 
main.py --> Main file where all operations work together in sync to run App 

auth2.py --> Create and Verify access user's token. Make sure current user is authenticated after logging in. 

database.py --> intializes engine to connect to SQL database

models.py -->  Provides Pydantic models of how data should be organized when sending information to a database 

schemas.py --> List schemas for how payload data should be organized when performing a CRUD operation to server and client

utils.py --> Password hashing and encryption 

auth.py --> Fastapi Oauth2 code to login user

post.py --> Contains CRUD operation decorators to get posts, get a specific post, delete a post, update a post, and create a post

user.py --> Contains CRUD operation decorators to get user information and create a user 

tests.py --> runs tests on every function/operation on the app. 

