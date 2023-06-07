from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def login():
    return "Signup"

@auth.route('/login')
def login():
    return "Login"

@auth.route('/logout')
def login():
    return "Logout"