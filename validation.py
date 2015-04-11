import re


def valid_username(username):
    name_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    match = name_re.match(username)
    if match:
        return True
    else:
        return False

def valid_password(password):
    password_re = re.compile(r"^.{3,20}$")
    match = password_re.match(password)
    if match:
        return True
    else:
        return False

def valid_email(email):
    email_re = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
    match = email_re.match(email)
    if match:
        return True
    else:
        return False



