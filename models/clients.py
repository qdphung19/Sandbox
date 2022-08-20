from models.basemodel import BaseModel, db


class Clients(BaseModel):
    __tablename__ = "clients"

    client_id = db.Column(db.Integer, primary_key=True)
    client_nom = db.Column(db.String(64))
    client_prenom = db.Column(db.String(64))
    client_domain = db.Column(db.String(64), unique=True)
    adresse = db.Column(db.String(128))
    code_postal = db.Column(db.String(128))
    ville = db.Column(db.String(128))
    pays = db.Column(db.String(64), default="France")

    #Labos - s'occuper - Clients: one to many
    labo_id = db.Column(db.Integer, db.ForeignKey("labos.labo_id"))

    # Clients - Echantillons - Order: one to many
    order_id = db.relationship("Orders", backref="clients", lazy=True)

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