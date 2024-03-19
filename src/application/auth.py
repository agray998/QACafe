import flask_login
from hashlib import scrypt
from os import urandom
from base64 import b64encode

login_manager = flask_login.LoginManager()

@login_manager.user_loader
def user_loader():
    pass

@login_manager.request_loader
def request_loader():
    pass

def hash_pword(password):
    salt = urandom(16)
    p_hash = scrypt(password, salt=salt, n = 2, r = 8, p = 1) # See RFC7914
    encoded = b64encode(p_hash).decode('utf-8') # Ensures bytes obtained from scrypt can be stored as a string
    return encoded, b64encode(salt).decode('utf-8') # return hashed and encoded password, as well as salt, to be stored in db

