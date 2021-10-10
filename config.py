from os import getenv

SECRET_KEY = getenv("123")
DB_NAME = getenv("ssis-webapp")
DB_USERNAME = getenv("root")
DB_PASSWORD = getenv("")
DB_HOST = getenv("localhost")
DB_PORT = getenv("3306")
DB_AUTH = getenv("")