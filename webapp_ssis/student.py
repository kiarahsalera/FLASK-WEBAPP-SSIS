from flask import Blueprint, render_template

student = Blueprint('student', __name__)


@student.route("/student/student", methods=['GET'])
def student_blueprint():
    return render_template('student.html')

