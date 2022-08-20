from models.basemodel import BaseModel, db
import datetime


class Orders(BaseModel):
    __tablename__ = "orders"

    order_id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())

    # Clients - Echantillons - Order:
    client_id = db.Column(db.Integer, db.ForeignKey('clients.client_id'))
    # client = db.relationship("Clients", backref="orders", lazy=True)
    echantillon_id = db.Column(db.Integer, db.ForeignKey('echantillons.echantillon_id'))
    echantillon = db.relationship("Echantillons", backref=db.backref("orders", uselist=False)) # one-to-one
    # labo_id = db.Column(db.Integer, db.ForeignKey('labos.labo_id'))
    # labo = db.relationship("Labos", backref="orders", lazy=True)



    def __init__(self):
        pass

    def __str__(self):
        return f'Order: {self.echantillon.dossier_ref} - {self.clients.client_nom} {self.clients.client_prenom} - {self.clients.client_domain}'
