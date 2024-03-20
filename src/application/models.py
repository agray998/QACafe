# TODO: Create SQLAlchemy Classes
from application import db
from flask_login import UserMixin

class Site(db.Model):
    ...

class StaffMember(db.Model):
    ...

class SiteAdmin(db.Model, UserMixin):
    ...

