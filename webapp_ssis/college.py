from flask import Blueprint, render_template, request, flash, redirect, url_for

college = Blueprint('college', __name__)

@college.route("/college", methods=['GET', 'POST'])
def displayCollegePage():
    return render_template('college.html')