from flask import Blueprint, render_template, redirect, url_for,flash, request
import webapp_ssis.functions as db
from .utils import add_colleges,update_college
college = Blueprint('college', __name__)


@college.route("/college", methods=['GET', 'POST'])
def displayCollegePage():
    college = db.College.display_college()
    course = db.Course.display_course()
    student = db.Student.display_students()
    return render_template('college.html', 
                                college = [college,student,course],
                                datacount = f'{len(college)} College')

@college.route('/college/search', methods=['GET', 'POST'])
def search() -> str:
    if request.method == 'POST':

        user_input = request.form.get('user-input')
        field = request.form.get('field')
        print(user_input,field)

        if field == 'select':
            result = db.College().search(keyword=user_input)
        elif field == 'college_code':
            result = db.College().search(keyword=user_input, field='college_code')
        elif field == 'colcode_name':
            result = db.College().search(keyword=user_input, field='colcode_name')
        else:
            result = []

        if len(result) != 0:
            return render_template('college.html', 
                                    college=[result],
                                    datacount = f'Search Result: {len(result)}'
                                   )
    else:
        return redirect(url_for('college.displayCollegePage'))



@college.route("/college/add_college", methods=['GET', 'POST'])
def addCollege() -> str:
    if request.method == 'POST':
        college = {
            'college_code': request.form.get('college_code'),
            'colcode_name': request.form.get('colcode_name')
        }
        add_colleges(college)
        flash(f'{college["college_code"]} added succesfully!', 'success')
        return redirect(url_for('college.displayCollegePage'))
    else:
        return redirect(url_for('college.displayCollegePage'))



@college.route('/college/delete/<string:college_code>')
def delete(college_code: str) -> str:
    try:
        db.College().delete(college_code)
        flash(f'{college_code} deleted from the database.', 'info')
        return redirect(url_for("college.displayCollegePage"))
    except:
        flash(f'{college_code} cannot be deleted. Students or courses are registered under the selected college.', 'danger')
        return redirect(url_for('college.colleges'))

@college.route("/college/edit_college/<string:college_code>", methods=['GET', 'POST'])
def editCollege(college_code: str) -> str:
    if request.method == "POST":
        college = {
            'college_code': college_code,
            'colcode_name': request.form.get('colcode_name')
        }
        update_college(college)
        flash(f"{college_code} has been updated succesfully!", 'info')
        return redirect(url_for('college.displayCollegePage'))

