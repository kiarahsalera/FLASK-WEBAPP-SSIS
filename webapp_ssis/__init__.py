from flask import Flask
from flask_mysql_connector import MySQL
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, CLOUD_NAME, API_KEY, API_SECRET
import cloudinary
import cloudinary.uploader
import cloudinary.api
from os import getenv

mysql = MySQL


def create_app():
    app = Flask(__name__, instance_relative_config=True)
  

    app.config.from_mapping(
        SECRET_KEY = SECRET_KEY,
        MYSQL_USER = DB_USERNAME,
        MYSQL_PASSWORD = DB_PASSWORD,
        MYSQL_DATABASE=DB_NAME,
        MYSQL_HOST=DB_HOST
    )

    cloudinary.config(
    cloud_name = getenv('CLOUD_NAME'),
    api_key = getenv('API_KEY'),
    api_secret = getenv('API_SECRET')
    )
 
    from .college import college
    from .course import course
    from .student import student


    app.register_blueprint(student, url_prefix="/")
    app.register_blueprint(course, url_prefix="/")
    app.register_blueprint(college, url_prefix="/")

    return app


 