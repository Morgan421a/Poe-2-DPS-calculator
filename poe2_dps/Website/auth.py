from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route('/login')
def login():
    return "<h1>login page</h1>"

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign up</p>"