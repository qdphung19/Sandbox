from models.basemodel import BaseModel, db


class PointCollectes(BaseModel):
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