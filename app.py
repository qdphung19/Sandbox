from flask import Flask
from flask_migrate import Migrate
from flask_admin import Admin, expose, AdminIndexView
from util import count_employes


# from flask.ext.babelex import Babel
# pour environment Windows
# from backup.backup import backup, compress_file, extract_file, filename


def load_views(app):
    from views.index import index_view
    app.register_blueprint(index_view, url_prefix='/')

    from views.submit import submit_view
    app.register_blueprint(submit_view, url_prefix="/")

    from views.login import login_view
    app.register_blueprint(login_view, url_prefix="/")

    from views.search import search_view
    app.register_blueprint(search_view, url_prefix="/")

    from views.backup import backup_view
    app.register_blueprint(backup_view, url_prefix="/")


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

class MyAdminIndexView(AdminIndexView):
    @expose("/")
    def index(self):
        return self.render('admin/adminindex.html', msg = count_employes())

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.cfg")
    migrate = Migrate()
    admin = Admin(name="Dashboard",
                  template_mode="bootstrap4",
                  index_view=MyAdminIndexView())
    # babel = Babel()

    with app.app_context():
        from models.basemodel import db

        load_views(app)
        db.init_app(app)
        # db.create_all()   # create all table
        migrate.init_app(app, db)
        admin.init_app(app)
        # babel.init_app(app)
        load_admin_view(admin, db)
        # pour environment Windows
        # backup('127.0.0.1', 'test', 'postgres', 'admin')
        # print(filename)
        # compress_file('backup-11082022-1500.dmp')
        # extract_file('backup-11082022-1500.dmp.gz')
        # print('ok')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
