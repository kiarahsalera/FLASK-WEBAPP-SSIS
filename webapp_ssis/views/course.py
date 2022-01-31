from flask import Blueprint, render_template, redirect, url_for,flash, request
import webapp_ssis.functions as db
from .utils import add_courses,update_course

course = Blueprint('course', __name__)


@course.route("/course", methods=['GET', 'POST'])
def displayCoursePage():
    course = db.Course.display_course()
    student = db.Student.display_students()
    college = db.College.display_college()
    return render_template('course.html', 
                                data = [course,student,college],
                                datacount = f'{len(course)} Course')

@course.route('/course/search', methods=['GET', 'POST'])
def search() -> str:
    if request.method == 'POST':

        user_input = request.form.get('user-input')
        field = request.form.get('field')
        print(user_input,field)

        if field == 'select':
            result = db.Course().search(keyword=user_input)
        elif field == 'code':
            result = db.Course().search(keyword=user_input, field='code')
        elif field == 'code_name':
            result = db.Course().search(keyword=user_input, field='code_name')
        elif field == 'college_name':
            result = db.Course().search(keyword=user_input, field='college_name')
        else:
            result = []

        if len(result) != 0:
            return render_template('course.html', 
                                    data=[result],
                                    datacount = f'Search Result: {len(result)}'
                                   )
    else:
        return redirect(url_for('course.displayCoursePage'))



@course.route("/course/add_course", methods=['GET', 'POST'])
def addCourse() -> str: 
    if request.method == 'POST':
        course = {
            'code': request.form.get('code'),
            'code_name': request.form.get('code_name'),
            'college_name': request.form.get('college_name')
        }
        add_courses(course)
        flash(f'{course["code"]} added succesfully!', 'success')
        return redirect(url_for("course.displayCoursePage"))
    else:
        return redirect(url_for("course.displayCoursePage"))



@course.route('/course/delete/<string:code>')
def delete(code: str) -> str:
    try:
        db.Course().delete(code)
        flash(f'{code} deleted from the database.', 'info')
        return redirect(url_for("course.displayCoursePage"))
    except:
        flash(f'{code} cannot be deleted. Students are enrolled in this program', 'danger')
        return redirect(url_for("course.displayCoursePage")) 


@course.route("/course/edit_course/<string:code>", methods=['GET', 'POST'])
def editCourse(code: str) -> str:
    if request.method == "POST":
        course = {
            'code': code,
            'code_name': request.form.get('code_name'),
            'college_name': request.form.get('college_name')
        }
        update_course(course)
        flash(f"{code} has been updated succesfully!", 'info')
        return redirect(url_for('course.displayCoursePage'))
    else:
        return redirect(url_for('course.displayCoursePage'))
