import app.db_mysql as db
import re

def validate_username(username):
    errors = []
    if not username:
        errors.append('No username provided')
    elif len(username) < 6:
        errors.append('Username must have atleast 6 characters')
    elif db.checkUserNameExists(username):
        errors.append('Username exists')
    return errors

def validate_email(email):
    errors = []
    if not email:
        errors.append('No email address specified')
    elif len(email)<7:
        errors.append('Email address too short, must have atleast 8 characters')
    elif not re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email):
        errors.append('Invalid email address')

    return errors

def validate_pwd(pwd):
    errors = []
    if not pwd:
        errors.append('Password cannot be blank')
    elif len(pwd) < 6:
        errors.append('Password must have atleast 6 characters')
    return errors


