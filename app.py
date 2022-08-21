from flask import Flask
from flask_migrate import Migrate
from flask_admin import Admin
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


def create_app():

    from views.admin.my_admin_index_view import MyAdminIndexView

    app = Flask(__name__)
    app.config.from_pyfile("config.cfg")
    migrate = Migrate()
    admin = Admin(name="Dashboard",
                  template_mode="bootstrap4",
                  index_view=MyAdminIndexView())
    # babel = Babel()

    with app.app_context():
        from models.basemodel import db
        from views.admin.load_admin_view import load_admin_view

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
