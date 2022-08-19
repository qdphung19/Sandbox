from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.dialects import postgresql
import enum
# from pymongo import MongoClient

# mongo = MongoClient("localhost", 27017)
# dbmongo = mongo.test   # DB test from local mongo server, DB name = flask
db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True
    db = db
    # dbmongo = dbmongo
    id = db.Column(db.Integer, primary_key=True)


class SexEnum(enum.Enum):
    Male = "Male"
    Female = "Female"
    Autre = "Autre"


class SexEnumEnfances(enum.Enum):
    Male = "Male"
    Female = "Female"
    Autre = "Autre"


class Enfances(db.Model):
    __tablename__ = "enfances"

    enfance_id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(64), nullable=False)
    prenom = db.Column(db.String(64), nullable=False)
    date_de_naissance = db.Column(db.DateTime)
    sex = db.Column(db.Enum(SexEnumEnfances))

    def __init__(self, nom, prenom, date_de_naissance, sex):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sex = sex


employes_enfances = db.Table('employes_enfances',
                              db.Column('employe_id', db.Integer, db.ForeignKey("employes.employe_id"), primary_key=True),
                              db.Column('enfance_id', db.Integer, db.ForeignKey("enfances.enfance_id"), primary_key=True)
                              )

class Employes(db.Model):
    __tablename__ = "employes"

    employe_id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(32), nullable=False)
    prenom = db.Column(db.String(32), nullable=False)
    date_de_naissance = db.Column(db.DateTime, nullable=False)
    sex = db.Column(db.Enum(SexEnum))
    adresse = db.Column(db.String(128), nullable=False)
    salaire = db.Column(db.Float)

    # -------- Mutually Dependent Rows----------------------------------------------------------------------------------
    # Employes - travailler - Labos: one to many
    labo_id = db.Column(db.Integer, db.ForeignKey("labos.labo_id"))

    # Employes - gérér - Labos:
    # rien ici

    # -------- END -----------------------------------------------------------------------------------------------------


    # Employes - surveiller - Employes
    # self referential relationship
    surveille_id = db.Column(db.Integer, db.ForeignKey("employes.employe_id"))
    surveille_par = db.relationship('Employes', remote_side=[employe_id])

    # Employes - participer - Processus: many to many
    processus = db.relationship("Processus", secondary="employes_processus", lazy='subquery',
                                backref=db.backref("employes", lazy=True))

    # Employes - avoir - Enfances: many to many
    enfances = db.relationship("Enfances", secondary="employes_enfances", lazy='subquery',
                               backref=db.backref("employes", lazy=True))

    def __init__(self, nom, prenom, date_de_naissance, sex,  salaire, adresse, labo_id, surveille_id):
        self.date_de_naissance = date_de_naissance
        self.sex = sex
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.adresse = adresse
        self.labo_id = labo_id
        self.surveille_id = surveille_id

    def __str__(self):
        return f'{self.nom} {self.prenom}'


employes_processus = db.Table('employes_processus',
                              db.Column('employe_id', db.Integer, db.ForeignKey("employes.employe_id"), primary_key=True),
                              db.Column('processus_id', db.Integer, db.ForeignKey("processus.processus_id"), primary_key=True)
                              )

class Labos(db.Model):
    __tablename__ = "labos"

    labo_id = db.Column(db.Integer, primary_key=True)
    labo_nom = db.Column(db.String(32), nullable=False)
    labo_adresse = db.Column(db.String(128))

    # -------- Mutually Dependent Rows----------------------------------------------------------------------------------
    # Labos (1,1) - gérer - Employes (0,1): One to One
    responsable_id = db.Column(db.Integer, db.ForeignKey("employes.employe_id"), nullable=False)
    # Mutually Dependent Rows: post_update=True
    # One to One: uselist=False
    # responsable = db.relationship("Employes", foreign_keys="[Labos.responsable_id]" , backref=db.backref("labo_responsable", uselist=False), post_update=True)
    responsable = db.relationship("Employes", foreign_keys="[Labos.responsable_id]" , uselist=False, post_update=True)
    # date_deput = db.Column(db.DateTime, nullable=False)

    # Labos - travailler - Employes: one to many
    employes = db.relationship("Employes", backref='labos', lazy=True, foreign_keys="[Employes.labo_id]")

    # -------- END -----------------------------------------------------------------------------------------------------

    # Labos - avoir - PointCollecte: one to many
    point_collecte = db.relationship("PointCollecte", backref='labos', lazy=True)

    def __init__(self, labo_id, labo_nom, labo_adresse):
        self.labo_id = labo_id
        self.labo_nom = labo_nom
        self.labo_adresse = labo_adresse
        # self.date_deput = date_deput

    def __str__(self):
        return self.labo_nom


class PointCollecte(db.Model):
    __tablename__ = "point_collecte"

    point_collecte_id = db.Column(db.Integer, primary_key=True)
    point_collecte_adresse = db.Column(db.String(128))
    # Labos - avoir - PointCollecte: one to many
    labo_id = db.Column(db.Integer, db.ForeignKey("labos.labo_id"))

    def __init__(self, labo_adresse):
        self.labo_adresse = labo_adresse

class Processus(db.Model):
    __tablename__ = "processus"

    processus_id = db.Column(db.Integer, primary_key=True)
    processus_nom = db.Column(db.String(32), nullable=False)

    def __init__(self, processus_id, processus_nom):
        self.processus_id = processus_id
        self.processus_nom = processus_nom

    def __str__(self):
        return self.processus_nom
