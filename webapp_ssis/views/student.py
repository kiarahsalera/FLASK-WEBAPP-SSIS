from flask import Blueprint, render_template, redirect, url_for, flash, request
from .utils import save_image,update_student_record,delete_image,add_student
import webapp_ssis.functions as db



student = Blueprint('student', __name__)



@student.route('/')
@student.route("/student", methods=['GET', 'POST'])
def displayStudentPage():
    student = db. Student.display_students()
    course = db.Course.display_course()
    return render_template('student.html', 
                                data = [student,course],
                                datacount = f'{len(student)} Student')

@student.route('/student/search', methods=['GET', 'POST'])
def search() -> str:
    if request.method == 'POST':

        user_input = request.form.get('user-input')
        field = request.form.get('field')
        print(user_input,field)

        if field == 'select':
            result = db.Student().search(keyword=user_input)
        elif field == 'id_no':
            result = db.Student().search(keyword=user_input, field='id_no')
        elif field == 'first_name':
            result = db.Student().search(keyword=user_input, field='first_name')
        elif field == 'last_name':
            result = db.Student().search(keyword=user_input, field='last_name')
        elif field == 'course':
            result = db.Student().search(keyword=user_input, field='course')
        elif field == 'year_level':
            result = db.Student().search(keyword=user_input, field='year_level')
        elif field == 'gender':
            result = db.Student().search(keyword=user_input, field='gender')
        else:
            result = []

        if len(result) != 0:
            return render_template('student.html', 
                                    data=[result],
                                    datacount = f'Search Result: {len(result)}'
                                   )
    else:
        return redirect(url_for('student.displayStudentPage'))


@student.route("/student/add_student", methods=['GET', 'POST'])
def addStudent() -> str:
     if request.method == 'POST':
        image = request.files['selected-image']
        try:
            cloud_link = save_image(image)
        except Exception as e:
            print("Can't save image")
            print(e)
        
        student = {
            'id_no': request.form.get('id_no'),
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'course': request.form.get('course'),
            'year_level': request.form.get('year_level'),
            'gender': request.form.get('gender'),
            'photo' : cloud_link
        }
        added = add_student(student)
        if added:
            flash(f'{student["first_name"]} is added succesfully!', 'success')
        else:
            flash(f'{student["first_name"]} cannot be added. Make sure the ID is unique.', 'danger')
        return redirect(url_for('student.displayStudentPage'))



@student.route('/student/delete/<string:id_no>')
def delete(id_no: str) -> str:
    data=db.Student().get_student(id_no)
    delete_image(id_no)
    db.Student().delete(id_no)
    flash(f'{data[0]} deleted from the database.', 'info')
    return redirect(url_for('student.displayStudentPage'))


@student.route('/student/edit_student/<string:id_no>', methods=['GET', 'POST'])
def editStudent(id_no: str) -> str:
    if request.method == 'POST':
        image = request.files['selected-image']
        cloud_link = ''
        try:
            cloud_link = save_image(image)
        except Exception as e:
            print("Can't save image")
            print(e)
        
        if cloud_link:
            student = {
            'id_no': id_no,
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'course': request.form.get('course'),
            'year_level': request.form.get('year_level'),
            'gender': request.form.get('gender'),
            'photo' : cloud_link
            }
            update_student_record(student)
        else:
            student = {
            'id_no': id_no,
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'course': request.form.get('course'),
            'year_level': request.form.get('year_level'),
            'gender': request.form.get('gender'),
            'photo' : cloud_link
            }
            update_student_record(student)
        flash(f"{student['first_name']}'s data has been changed succesfully!", 'success')
        return redirect(url_for('student.displayStudentPage'))
    else:
        return redirect(url_for('student.displayStudentPage'))

