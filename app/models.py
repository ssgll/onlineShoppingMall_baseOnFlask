# -*-coding:utf-8-*-
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()


# 用户表
class user(db.Model, UserMixin):
    __table_name__ = "user"
    __table_args__ = {
        "mysql_charset": "utf8"
    }
    userID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(256))
    tel = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError("Password is not readable")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.userID

    def __repr__(self):
        return "<Username: {}>".format(self.username)
