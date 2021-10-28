from flask import Blueprint, render_template, redirect, url_for, request
import webapp_ssis.functions as db
import re

college = Blueprint('college', __name__)


@college.route("/college", methods=['GET', 'POST'])
def displayCollegePage():
    college = db.College.display_college()
    return render_template('college.html', 
                                college = [college],
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
def addCollege():
    if request.method == "POST":
        college_code = request.form['college_code'].upper()
        colcode_name = request.form['colcode_name'].capitalize()


        college = db.College(college_code,colcode_name)
        college.add_college()
        return redirect(url_for('college.displayCollegePage'))

@college.route("/college/delete_college", methods=["POST"]) 
def deleteCollege():
    if request.method == "POST":
        college_code = request.form.get('college_id_del')
        db.College.delete_college(college_code)
    
    return redirect(url_for("college.displayCollegePage"))

@college.route("/college/edit_college", methods=['GET', 'POST'])
def editCollege():
    if request.method == "POST":
        old_college_number = request.form['old_college_number']
        college_code = request.form['college_code'].upper()
        colcode_name = request.form['colcode_name'].capitalize()
     
        
        db.College.edit_college(college_code,colcode_name, old_college_number)
        return redirect(url_for('college.displayCollegePage'))

