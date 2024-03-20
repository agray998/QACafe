from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from application import db
from application.auth import hash_pword
from application.models import SiteAdmin
from base64 import b64decode

class CorrectPassword():
    def __init__(self, message = "Incorrect username or password supplied"):
        self.message = message

    def __call__(self, form, field):
        user = db.session.get(SiteAdmin, form.user_id.data)
        try:
            salt = b64decode(user.salt)
            if hash_pword(field.data, salt=salt)[0] == user.password:
                return True
        except:
            pass
        raise ValidationError(message=self.message)

class LoginForm(FlaskForm):
    user_id = StringField("User ID", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired(), CorrectPassword()])
    login = SubmitField("Login")