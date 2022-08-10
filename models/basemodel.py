from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient


mongo = MongoClient("localhost", 27017)
dbmongo = mongo.test   # DB test from local mongo server, DB name = flask
dbpsql = SQLAlchemy()



class BaseModel(dbpsql.Model):
    __abstract__ = True
    dbpsql = dbpsql
    dbmongo = dbmongo
    id = dbpsql.Column(dbpsql.Integer, primary_key=True)