#A set of validation functions for signup, login, training, quizzes and exams.

import re
#Signup validations
def validate_username(username):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{8,20}$")
    if USER_RE.match(username):
        return username
    else:
        return False

def validate_password(password):
    PWD_RE = re.compile(r"^.{8,20}$")
    if PWD_RE.match(password):
        return password
    else:
            return False

def validate_verify(password, verify):
    if password == verify:
        return verify
    else:
        return False

def validate_email(email):
    if not email:
        return ""

    EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
    if EMAIL_RE.match(email):
        return email
    else:
        return False




#Login validations
