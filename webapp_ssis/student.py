from flask import Blueprint, render_template, redirect, url_for, request, flash
import webapp_ssis.functions as db
import re

student = Blueprint('student', __name__)


@student.route("/student", methods=['GET', 'POST'])
def displayStudentPage():
    student = db.Student.display_students()
    return render_template('student.html',student=student)


@student.route("/student/add_student", methods=['GET', 'POST'])
def addStudent():
    if request.method == "POST":
        id_no = request.form['id_no']
        first_name = request.form['first_name'].capitalize()
        last_name = request.form['last_name'].capitalize()
        course = request.form['course'].upper()
        year_level = request.form['year_level']
        gender = request.form['gender']

     

        student = db.Student(id_no, first_name, last_name, course, year_level, gender)
        student.add_student()
        return redirect(url_for('student.displayStudentPage'))

@student.route("/student/delete_student", methods=["POST"]) 
def deleteStudent():
    if request.method == "POST":
        student_id = request.form.get('id_no')
        db.Student.delete_student(student_id)
    
    return redirect(url_for("student.displayStudentPage"))

@student.route("/student/edit_student", methods=['GET', 'POST'])
def editStudent():
    if request.method == "POST":
        old_id_number = request.form['old_id_number']
        id_no = request.form['id_no']
        first_name = request.form['first_name'].capitalize()
        last_name = request.form['last_name'].capitalize()
        course = request.form['course'].upper()
        year_level = request.form['year_level']
        gender = request.form['gender']


        db.Student.edit_student(id_no, first_name, last_name, course, year_level, gender, old_id_number)
        return redirect(url_for('student.displayStudentPage'))
