from os import getenv

SECRET_KEY = getenv("SECRET_KEY")
DB_NAME = getenv("DB_NAME")
DB_USERNAME = getenv("DB_USERNAME")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_HOST = getenv("DB_HOST")
DB_PORT = getenv("DB_PORT")
DB_AUTH = getenv("DB_AUTH")

CLOUD_NAME = getenv("CLOUD_NAME")
API_KEY = getenv("API_KEY")
API_SECRET = getenv("API_SECRET")
PHOTO_UPLOAD = getenv("PHOTO_UPLOAD")
