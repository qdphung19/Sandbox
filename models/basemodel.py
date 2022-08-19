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


# employes_enfances = db.Table('employes_enfances',
#                               db.Column('employe_id', db.Integer, db.ForeignKey("employes.employe_id"), primary_key=True),
#                               db.Column('enfance_id', db.Integer, db.ForeignKey("enfances.enfance_id"), primary_key=True)
#                               )
#
#
# employes_processus = db.Table('employes_processus',
#                               db.Column('employe_id', db.Integer, db.ForeignKey("employes.employe_id"), primary_key=True),
#                               db.Column('processus_id', db.Integer, db.ForeignKey("processus.processus_id"), primary_key=True)
#                               )
