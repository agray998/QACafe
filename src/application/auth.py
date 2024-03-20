from application import login_manager
from hashlib import scrypt
from os import urandom
from base64 import b64encode
from application.models import SiteAdmin
from application import db

@login_manager.user_loader
def user_loader(user_id):
    return db.session.get(SiteAdmin, user_id)

@login_manager.request_loader
def request_loader():
    pass

def hash_pword(password, salt=""):
    salt = salt if salt else urandom(16)
    p_hash = scrypt(password, salt=salt, n = 2, r = 8, p = 1) # See RFC7914
    encoded = b64encode(p_hash).decode('utf-8') # Ensures bytes obtained from scrypt can be stored as a string
    return encoded, b64encode(salt).decode('utf-8') # return hashed and encoded password, as well as salt, to be stored in db

