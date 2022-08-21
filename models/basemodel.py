from flask_sqlalchemy import SQLAlchemy
import enum
# from pymongo import MongoClient

# mongo = MongoClient("localhost", 27017)
# dbmongo = mongo.test   # DB test from local mongo server, DB name = flask
db = SQLAlchemy()


class BaseModel(db.Model):

    __abstract__ = True
    db = db
    # dbmongo = dbmongo
    # id = db.Column(db.Integer, primary_key=True)
