from flask import Blueprint, render_template, redirect, url_for, request
import webapp_ssis.functions as db
import re

course = Blueprint('course', __name__)


@course.route("/course", methods=['GET', 'POST'])
def displayCoursePage():
    course = db.Course.display_course()
    return render_template('course.html',course=course)


@course.route("/course/add_course", methods=['GET', 'POST'])
def addCourse():
    if request.method == "POST":
        code = request.form['code'].upper()
        code_name = request.form['code_name'].capitalize()
        college_name = request.form['college_name'].upper()

     

        course = db.Course(code, code_name, college_name)
        course.add_course()
        return redirect(url_for('course.displayCoursePage'))

@course.route("/course/delete_course", methods=["POST"]) 
def deleteCourse():
    if request.method == "POST":
        code = request.form.get('course_id_del')
        db.Course.delete_course(code)
    
    return redirect(url_for("course.displayCoursePage"))

@course.route("/course/edit_course", methods=['GET', 'POST'])
def editCourse():
    if request.method == "POST":
        old_course_number = request.form['old_course_number']
        code = request.form['code'].upper()
        code_name = request.form['code_name'].capitalize()
        college_name = request.form['college_name'].upper()
        


        db.Course.edit_course(code, code_name, college_name, old_course_number)
        return redirect(url_for('course.displayCoursePage'))

