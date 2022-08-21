def load_admin_view(admin, db):
    # from models.basemodel import
    from models.employes import Employes
    from models.labos import Labos
    from models.proccesus import Processus
    from models.point_collectes import PointCollectes
    from models.enfances import Enfances
    from models.clients import Clients
    from models.echantillons import Echantillons
    from models.samples import Samples
    from models.orders import Orders
    from models.resultats import Resultats

    from flask_admin.contrib.sqla import ModelView
    class EmployesViewConfig(ModelView):
        can_view_details = True
        details_modal = True
        column_list = ('employe_id', 'nom', 'prenom', 'date_de_naissance', 'sex', 'adresse', 'surveille_par', 'labos')
        # column_exclude_list = ['salaire']
        column_filters = ['employe_id', 'nom']
        column_searchable_list = ['employe_id', 'nom', 'prenom']
        column_labels = {
            'employe_id': 'employe_ID'
        }

    class LabosViewConfig(ModelView):
        column_display_pk = True
        form_excluded_columns = ['employes', 'point_collecte', 'clients']

    admin.add_view(EmployesViewConfig(Employes, db.session))
    admin.add_view(LabosViewConfig(Labos, db.session))
    admin.add_view(ModelView(Processus, db.session))
    admin.add_view(ModelView(PointCollectes, db.session))
    admin.add_view(ModelView(Enfances, db.session))
    admin.add_view(ModelView(Clients, db.session))
    admin.add_view(ModelView(Orders, db.session))
    admin.add_view(ModelView(Echantillons, db.session))
    admin.add_view(ModelView(Samples, db.session))
    admin.add_view(ModelView(Resultats, db.session))