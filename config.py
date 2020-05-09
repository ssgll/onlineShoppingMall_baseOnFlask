#! coding:utf-8
import os
from datetime import timedelta
import mysql.connector
import redis


class Config(object):
    DEBUG = True
    PORT = 5000
    HOST = "127.0.0.1"
    BASE_DIR = os.getcwd()
    FLASK_ENV = "development"
    TEMPLATE_FOLDER = os.path.join(BASE_DIR, "templates")
    STATIC_FOLDER = os.path.join(BASE_DIR, "static")

    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://ssgll:383687@127.0.0.1/project1?charset=utf8"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    PERMANENT_SESSION_LIFETIME = timedelta(minutes=1)
    SECRET_KEY = 'OsNI7p!$INtD^YiqcevM4clwF!8Ts@IK&FHRsQ515SfK4f6NEI!PC^^Nfcfe^Fre'
    SESSION_TYPE = "redis"
    redisPool = redis.ConnectionPool(host="127.0.0.1", port=6379, password="383687")
    SESSION_REDIS = redis.Redis(connection_pool=redisPool)
    SESSION_USE_SIGNER = False
    SESSION_KEY_PREFIX = "session:"
    SESSION_REFRESH_EACH_REQUEST = True


class Development(Config):
    pass


class Testing(Config):
    pass


config = {
    "Config": Config,
    "Development": Development,
    "Testing": Testing,
    "Default": Config,
}