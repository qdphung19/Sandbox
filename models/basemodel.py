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
    # id = db.Column(db.Integer, primary_key=True)


class EnumSexEmployes(enum.Enum):
    Male = "Male"
    Female = "Female"
    Autre = "Autre"


class EnumSexEnfances(enum.Enum):
    Male = "Male"
    Female = "Female"
    Autre = "Autre"


class Enfances(db.Model):
    __tablename__ = "enfances"

    enfance_id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(64))
    prenom = db.Column(db.String(64))
    date_de_naissance = db.Column(db.DateTime)
    sex = db.Column(db.Enum(EnumSexEnfances))

    def __init__(self, nom, prenom, date_de_naissance, sex):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sex = sex

    def __str__(self):
        return f'{self.nom} {self.prenom}'


employes_enfances = db.Table('employes_enfances',
                              db.Column('employe_id', db.Integer, db.ForeignKey("employes.employe_id"), primary_key=True),
                              db.Column('enfance_id', db.Integer, db.ForeignKey("enfances.enfance_id"), primary_key=True)
                              )

class Employes(db.Model):
    __tablename__ = "employes"

    employe_id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(32))
    prenom = db.Column(db.String(32))
    date_de_naissance = db.Column(db.DateTime)
    sex = db.Column(db.Enum(EnumSexEmployes))
    adresse = db.Column(db.String(128))
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
    labo_nom = db.Column(db.String(32))
    labo_adresse = db.Column(db.String(128))

    # -------- Mutually Dependent Rows----------------------------------------------------------------------------------
    # Labos (1,1) - gérer - Employes (0,1): One to One
    responsable_id = db.Column(db.Integer, db.ForeignKey("employes.employe_id"))
    # Mutually Dependent Rows: post_update=True
    # One to One: uselist=False
    # responsable = db.relationship("Employes", foreign_keys="[Labos.responsable_id]" , backref=db.backref("labo_responsable", uselist=False), post_update=True)
    responsable = db.relationship("Employes", foreign_keys="[Labos.responsable_id]" , uselist=False, post_update=True)

    # Labos - travailler - Employes: one to many
    employes = db.relationship("Employes", backref='labos', lazy=True, foreign_keys="[Employes.labo_id]")

    # -------- END -----------------------------------------------------------------------------------------------------

    # Labos - avoir - PointCollectes: one to many
    point_collecte = db.relationship("PointCollectes", backref='labos', lazy=True)

    # clients = db.relationship("Clients", backref='labos', lazy=True, foreign_keys="[Labos.labo_id]")
    clients = db.relationship("Clients", backref='labos', lazy=True)

    def __init__(self, labo_id, labo_nom, labo_adresse):
        self.labo_id = labo_id
        self.labo_nom = labo_nom
        self.labo_adresse = labo_adresse
        # self.date_deput = date_deput

    def __str__(self):
        return self.labo_nom


class PointCollectes(db.Model):
    __tablename__ = "point_collectes"

    point_collecte_id = db.Column(db.Integer, primary_key=True)
    point_collecte_nom = db.Column(db.String(128))
    point_collecte_adresse = db.Column(db.String(128))
    # Labos - avoir - PointCollectes: one to many
    labo_id = db.Column(db.Integer, db.ForeignKey("labos.labo_id"))

    def __init__(self, point_collecte_nom, point_collecte_adresse):
        self.point_collecte_nom = point_collecte_nom
        self.point_collecte_adresse = point_collecte_adresse

    def __str__(self):
        return self.point_collecte_nom

class Processus(db.Model):
    __tablename__ = "processus"

    processus_id = db.Column(db.Integer, primary_key=True)
    processus_nom = db.Column(db.String(32))
    processus_description = db.Column(db.String(256))

    def __init__(self, processus_nom, processus_description):
        self.processus_nom = processus_nom
        self.processus_description = processus_description

    def __str__(self):
        return self.processus_nom



class Clients(db.Model):
    __tablename__ = "clients"

    client_id = db.Column(db.Integer, primary_key=True)
    client_nom = db.Column(db.String(64))
    client_prenom = db.Column(db.String(64))
    client_domain = db.Column(db.String(64), unique=True)
    adresse = db.Column(db.String(128))
    code_postal = db.Column(db.String(128))
    ville = db.Column(db.String(128))
    pays = db.Column(db.String(64), default="France")

    labo_id = db.Column(db.Integer, db.ForeignKey("labos.labo_id"))

    def __init__(self, client_nom, client_prenom, client_domain, adresse, code_postal, ville, pays):
        self.client_nom = client_nom
        self.client_prenom = client_prenom
        self.client_domain = client_domain
        self.adresse = adresse
        self.code_postal = code_postal
        self.ville = ville
        self.pays = pays

    def __str__(self):
        return f'{self.client_nom} {self.client_prenom} - {self.client_domain}'