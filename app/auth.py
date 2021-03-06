from bottle import route, post, get, request, redirect
import bottle
import app.db_mysql as db
from app.settings import view
import app.validation as validation

@get('/login')
def login():
    return view("auth/login.html")

@post('/login')
def auth():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if db.authUser(username, password):
        ses = bottle.request.environ.get('beaker.session')
        ses['user'] = username
        return redirect('/library')
    else:
        return view("auth/login.html", error="Invalid login details")

@get('/logout')
def logout():
    ses = bottle.request.environ.get('beaker.session')
    ses.delete()
    bottle.redirect("/login")

@get('/register')
def registerForm():
    return view('auth/register.html')

@post('/register')
def register():
    errors = []
    username = request.forms.get('username')
    email = request.forms.get('email')
    pwd = request.forms.get('pwd')
    vpwd = request.forms.get('vpwd')

    errors += validation.validate_username(username)
    errors += validation.validate_email(email)
    errors += validation.validate_pwd(pwd)

    if(vpwd != pwd):
        errors.append('Verification password and password do not match');

    if errors:
        return view('auth/register.html', errors = errors, username=username, email=email, pwd=pwd)
    else:
        db.registerUser(username, pwd, email)
        return view('auth/register.html', registrationComplete=True)

@get('/resetPassword')
def resetPassword():
    return view('auth/resetPassword.html')

@post('/resetPassword')
def restPasswordSubmit():
    username = request.forms.get('username')
    db.checkUserNameExists(username)
    return view('auth/resetPassword.html')

