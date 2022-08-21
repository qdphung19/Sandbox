from models.basemodel import BaseModel, db
import datetime


class Orders(BaseModel):

    __tablename__ = "orders"

    order_id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, default=datetime.datetime.utcnow(), nullable=False)

    # Clients - Echantillons - Order:
    client_id = db.Column(db.Integer, db.ForeignKey('clients.client_id'), nullable=False)
    echantillon_id = db.Column(db.Integer, db.ForeignKey('echantillons.echantillon_id'), nullable=False)
    echantillon = db.relationship("Echantillons", backref=db.backref("orders", uselist=False)) # one-to-one



    def __init__(self):
        pass

    def __str__(self):
        return f'Order: {self.echantillon.dossier_ref} - {self.clients.client_nom} {self.clients.client_prenom} - {self.clients.client_domain}'
