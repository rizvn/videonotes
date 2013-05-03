from bottle import route, post, get, request, redirect
import bottle
import app.db_mysql as db
from app.settings import view

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

    if not username:
        errors.append('No username provided')
    elif len(username) < 6:
        errors.append('Username must be 6 characters long')
    elif db.checkUserNameExists(username):
        errors.append('Username exists')


    return view('auth/register.html', errors = errors)

@get('/resetPassword')
def resetPassword():
    return view('auth/resetPassword.html')