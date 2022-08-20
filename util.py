from models.basemodel import db
from models.employes import Employes
from models.labos import Labos
from sqlalchemy import func

def count_employes():
    # return Labos.query.join(Employes, Employes.labo_id.__eq__(Labos.labo_id), isouter=True)\
    #     .add_column(func.count(Employes.employe_id))\
    #     .group_by(Labos.labo_id, Labos.labo_nom)\
    #     .all()

    return db.session.query(Labos.labo_id, Labos.labo_nom, func.count(Employes.employe_id))\
        .join(Employes, Employes.labo_id.__eq__(Labos.labo_id), isouter=True)\
        .group_by(Labos.labo_id, Labos.labo_nom)\
        .order_by(Labos.labo_id)\
        .all()