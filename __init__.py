from flask import Flask
from flask_migrate import Migrate


def load_views(app):
    from views.index import index_view
    app.register_blueprint(index_view, url_prefix='/')

    from views.submit import submit_view
    app.register_blueprint(submit_view, url_prefix="/")


def get_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.cfg")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    with app.app_context():
        load_views(app)
        from models.basemodel import dbpsql
        # db.create_all()  non !!!
        dbpsql.init_app(app)
        migrate = Migrate(app, dbpsql)
        print(migrate)
    return app


if __name__ == '__main__':
    app = get_app()
    app.run(debug=True)