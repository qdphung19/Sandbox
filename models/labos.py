from models.basemodel import BaseModel, db


class Labos(BaseModel):

    __tablename__ = "labos"

    labo_id = db.Column(db.Integer, primary_key=True)
    labo_nom = db.Column(db.String(32), nullable=False, unique=True)
    labo_adresse = db.Column(db.String(128), nullable=False)

    # -------- Mutually Dependent Rows----------------------------------------------------------------------------------
    # Labos (1,1) - gérer - Employes (0,1): One to One
    responsable_id = db.Column(db.Integer, db.ForeignKey("employes.employe_id"), nullable=False)
    # Mutually Dependent Rows: post_update=True
    # One to One: uselist=False
    responsable = db.relationship("Employes", foreign_keys="[Labos.responsable_id]" , backref=db.backref("labo_responsable", uselist=False), post_update=True)
    # responsable = db.relationship("Employes", foreign_keys="[Labos.responsable_id]" , uselist=False, post_update=True)

    # Labos - travailler - Employes: one to many
    employes = db.relationship("Employes", backref='labos', lazy=True, foreign_keys="[Employes.labo_id]")

    # -------- END -----------------------------------------------------------------------------------------------------

    # Labos - avoir - PointCollectes: one to many
    point_collecte = db.relationship("PointCollectes", backref='labos', lazy=True)

    # Labos - s'occuper - Clients: one to many
    # clients = db.relationship("Clients", backref='labos', lazy=True, foreign_keys="[Labos.labo_id]")
    clients = db.relationship("Clients", backref='labos', lazy=True)

    # Labos - Clients - Echantillons - Order:
    # order_id = db.relationship("Orders", backref="labos", lazy=True)

    def __init__(self, labo_id, labo_nom, labo_adresse, responsable_id):
        self.labo_id = labo_id
        self.labo_nom = labo_nom
        self.labo_adresse = labo_adresse
        self.responsable_id = responsable_id

    def __str__(self):
        return self.labo_nom