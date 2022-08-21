from models.basemodel import BaseModel, db
import enum

class EnumSexEmployes(enum.Enum):
    Male = "Male"
    Female = "Female"
    Autre = "Autre"


employes_enfances = db.Table('employes_enfances',
                              db.Column('employe_id', db.Integer, db.ForeignKey("employes.employe_id"), primary_key=True),
                              db.Column('enfance_id', db.Integer, db.ForeignKey("enfances.enfance_id"), primary_key=True)
                              )


employes_processus = db.Table('employes_processus',
                              db.Column('employe_id', db.Integer, db.ForeignKey("employes.employe_id"), primary_key=True),
                              db.Column('processus_id', db.Integer, db.ForeignKey("processus.processus_id"), primary_key=True)
                              )

class Employes(BaseModel):

    __tablename__ = "employes"

    employe_id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(32), nullable=False)
    prenom = db.Column(db.String(32), nullable=False)
    date_de_naissance = db.Column(db.DateTime, nullable=False)
    sex = db.Column(db.Enum(EnumSexEmployes), nullable=False)
    adresse = db.Column(db.String(128), nullable=False)
    salaire = db.Column(db.Float)

    # -------- Mutually Dependent Rows----------------------------------------------------------------------------------
    # Employes - travailler - Labos: one to many
    labo_id = db.Column(db.Integer, db.ForeignKey("labos.labo_id"), nullable=False)

    # Employes - gérér - Labos:
    # rien ici

    # -------- END -----------------------------------------------------------------------------------------------------


    # Employes - surveiller - Employes
    # self-referential relationship
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