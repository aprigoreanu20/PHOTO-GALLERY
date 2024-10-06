from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(30))
    name = db.Column(db.String(20))
    category = db.Column(db.String(20)) 
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(100), unique=True)
    firstName = db.Column(db.String(100))
    user_password = db.Column(db.String(300))
    gallery = db.relationship('Photo')
