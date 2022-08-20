from models.basemodel import BaseModel, db
import datetime


class Orders(BaseModel):
    __tablename__ = "orders"

    order_id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())

    client_id = db.Column(db.Integer, db.ForeignKey('clients.client_id'))
    labo_id = db.Column(db.Integer, db.ForeignKey('labos.labo_id'))
    echantillon_id = db.Column(db.Integer, db.ForeignKey('echantillons.echantillon_id'))
    # Labos - Clients - Echantillons - Order:
    echantillon = db.relationship("Echantillons", backref=db.backref("orders", uselist=False)) # one-to-one, no backref needed
    client = db.relationship("Clients", backref="orders", lazy=True)
    labo = db.relationship("Labos", backref="orders", lazy=True)



    def __init__(self):
        pass
