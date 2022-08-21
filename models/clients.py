from models.basemodel import BaseModel, db


class Clients(BaseModel):

    __tablename__ = "clients"

    client_id = db.Column(db.Integer, primary_key=True)
    client_nom = db.Column(db.String(64), nullable=False)
    client_prenom = db.Column(db.String(64), nullable=False)
    client_domain = db.Column(db.String(64), nullable=False, unique=True)
    adresse = db.Column(db.String(128), nullable=False)
    code_postal = db.Column(db.String(128), nullable=False)
    ville = db.Column(db.String(128), nullable=False)
    pays = db.Column(db.String(64), default="France", nullable=False)

    #Labos - s'occuper - Clients: one to many
    labo_id = db.Column(db.Integer, db.ForeignKey("labos.labo_id"), nullable=False)

    # Clients - Echantillons - Order: one to many
    order_id = db.relationship("Orders", backref="clients", lazy=True)

    def __init__(self, client_nom, client_prenom, client_domain, adresse, code_postal, ville, pays, labo_id):
        self.client_nom = client_nom
        self.client_prenom = client_prenom
        self.client_domain = client_domain
        self.adresse = adresse
        self.code_postal = code_postal
        self.ville = ville
        self.pays = pays
        self.labo_id = labo_id

    def __str__(self):
        return f'{self.client_nom} {self.client_prenom} - {self.client_domain}'