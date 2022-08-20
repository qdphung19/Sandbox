from models.basemodel import BaseModel, db


class Samples(BaseModel):
    __tablename__ = "samples"

    samples_id = db.Column(db.Integer, primary_key=True)
    echantillon_id = db.Column(db.Integer, db.ForeignKey("echantillons.echantillon_id"))
    samples_ref = db.Column(db.String(32))
    cuve_ref = db.Column(db.String(32))

    def __init__(self, samples_ref, cuve_ref):
        self.samples_ref = samples_ref
        self.cuve_ref = cuve_ref