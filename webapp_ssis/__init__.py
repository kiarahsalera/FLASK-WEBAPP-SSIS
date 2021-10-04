from flask import Flask, Blueprint, render_template


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    from .homepage import homepage
    from .college import college
    from .course import course
    from .student import student

    app.register_blueprint(homepage, url_prefix="/")
    app.register_blueprint(student, url_prefix="/")
    app.register_blueprint(course, url_prefix="/")
    app.register_blueprint(college, url_prefix="/")

    return app
