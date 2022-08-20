from models.basemodel import BaseModel, db


class Echantillons(BaseModel):
    __tablename__ = "echantillons"

    echantillon_id = db.Column(db.Integer, primary_key=True)
    dossier_ref = db.Column(db.String(32))
    # Echantillons - avoir - Samples: one to many
    samples = db.relationship("Samples", backref='echantillons', lazy=True)

    def __init__(self, dossier_ref):
        self.dossier_ref = dossier_ref
