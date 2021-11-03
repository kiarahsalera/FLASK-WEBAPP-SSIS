from flask import Blueprint, render_template, redirect, url_for, request, flash
import webapp_ssis.functions as db



student = Blueprint('student', __name__)



@student.route('/')
@student.route("/student", methods=['GET', 'POST'])
def displayStudentPage():
    student = db.Student.display_students()
    course = db.Course.display_course()
    return render_template('student.html', 
                                student = [student,course],
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
                                    student=[result],
                                    datacount = f'Search Result: {len(result)}'
                                   )
    else:
        return redirect(url_for('student.displayStudentPage'))


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


@student.route('/students/delete/<string:id_no>')
def delete(id_no: str) -> str:
    db.Student().delete(id_no)
    return redirect(url_for('student.displayStudentPage'))



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