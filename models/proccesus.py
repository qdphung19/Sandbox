from models.basemodel import BaseModel, db


class Processus(BaseModel):

    __tablename__ = "processus"

    processus_id = db.Column(db.Integer, primary_key=True)
    processus_nom = db.Column(db.String(32), nullable=False, unique=True)
    processus_description = db.Column(db.String(256))

    def __init__(self, processus_nom, processus_description):
        self.processus_nom = processus_nom
        self.processus_description = processus_description

    def __str__(self):
        return self.processus_nom