from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, SelectField
import webapp_ssis.functions as functions


class StudentForm(FlaskForm):
    id_no = StringField('ID', [validators.DataRequired()])
    first_name = StringField('Firstname', [validators.DataRequired()])
    last_name = StringField('Lastname', [validators.DataRequired()])
    course = StringField('Course', [validators.DataRequired()])
    year_level = SelectField('Year', [validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()])
    submit = SubmitField("Submit")

