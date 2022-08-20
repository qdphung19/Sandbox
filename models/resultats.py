from models.basemodel import BaseModel, db
import datetime


class Resultats(BaseModel):
    __tablename__ = "resultats"

    resultat_id = db.Column(db.Integer, primary_key=True)
    resultat_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())

    degree = db.Column(db.Float)
    glucose = db.Column(db.Float)
    ph = db.Column(db.Float)

    # Samples - Resultats : one to one
    sample_id = db.Column(db.Integer, db.ForeignKey('samples.sample_id'))
    sample = db.relationship("Samples", backref=db.backref("resultats", uselist=False))

    def __init__(self, degree, glucose, ph):
        self.degree = degree
        self.glucose = glucose
        self.ph = ph

    def __str__(self):
        return f'Résultat de {self.sample.samples_ref} - {self.sample.cuve_ref}'