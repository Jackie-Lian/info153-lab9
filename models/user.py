from db import db

class UserModel(db.Model):
    # name of table
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), unique=False, nullable=False)
    quote = db.Column(db.String(500), unique = False, nullable = False)
