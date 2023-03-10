from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


# ----------------- Create User ID---------------------
class User(UserMixin, db.Model):
    """ User model """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)

# db.create_all()


# -------------------- Save Message History------------------
class History(db.Model):
    """ Save Chat History """

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column('message', db.String(500))

    # db.create_all()
