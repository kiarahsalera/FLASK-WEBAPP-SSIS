from flask import Blueprint, render_template, request, flash, redirect, url_for

course = Blueprint('course', __name__)

@course.route("/course", methods=['GET', 'POST'])
def displayCoursePage():
    return render_template('course.html')