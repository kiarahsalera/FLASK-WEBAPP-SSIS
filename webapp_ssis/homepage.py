from flask import Blueprint, render_template, request, flash, redirect, url_for

homepage = Blueprint('homepage', __name__)

@homepage.route('/')
@homepage.route("/homepage", methods=['GET'])
def index():
    return render_template("index.html")
