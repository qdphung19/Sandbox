from flask import Flask
from flask_migrate import Migrate
from backup.backup import backup, compress_file, extract_file, filename


def load_views(app):
    from views.index import index_view
    app.register_blueprint(index_view, url_prefix='/')

    from views.submit import submit_view
    app.register_blueprint(submit_view, url_prefix="/")

    from views.login import login_view
    app.register_blueprint(login_view, url_prefix="/")

    from views.search import search_view
    app.register_blueprint(search_view, url_prefix="/")


def get_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.cfg")

    with app.app_context():
        load_views(app)
        from models.basemodel import dbpsql
        # db.create_all()  non !!!
        dbpsql.init_app(app)
        migrate = Migrate(app, dbpsql)
        # backup('127.0.0.1', 'test', 'postgres', 'admin')
        # print(filename)
        # compress_file('backup-11082022-1500.dmp')
        # extract_file('backup-11082022-1500.dmp.gz')
        # print('ok')
    return app


if __name__ == '__main__':
    app = get_app()
    app.run(debug=True)