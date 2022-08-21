from models.basemodel import BaseModel, db
import enum


class EnumSexEnfances(enum.Enum):
    Male = "Male"
    Female = "Female"
    Autre = "Autre"


class Enfances(BaseModel):

    __tablename__ = "enfances"

    enfance_id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(64), nullable=False)
    prenom = db.Column(db.String(64), nullable=False)
    date_de_naissance = db.Column(db.DateTime, nullable=False)
    sex = db.Column(db.Enum(EnumSexEnfances))

    def __init__(self, nom, prenom, date_de_naissance, sex):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sex = sex

    def __str__(self):
        return f'{self.nom} {self.prenom}'