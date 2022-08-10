from flask import Flask
from flask_migrate import Migrate

import gzip
import subprocess


def backup(host, dbname, user, password):
    # with gzip.open('backup.gz', 'wb') as f:
    # command = f'pg_dump -h {host} -d {dbname} -U {user} --no-password  -p 5432  -Fc -f D:\\test10.dmp'
    command = f'pg_dump -h {host} -p 5432 -d {dbname} -U {user} -Fc -f D:\\test10.dmp'
    # command = f'pg_dump'
    popen = subprocess.Popen(command, shell=True, env={
        'PGPASSWORD': password,
        'PATH': 'C:\Program Files\PostgreSQL\\12\\bin',
        'PGHOST': '127.0.0.1',
        'PGPORT': '5432'
                             })

    # for stdout_line in iter(popen.stdout.readline, ''):
    #     f.write(stdout_line.encode('utf-8'))

    # popen.stdout.close()
    popen.wait()

# def backup(host, dbname, user, password):
#     command = f'pg_dump -h {host} -d {dbname} -U {user} -p 5432  -Fc -f /tmp/table.dmp'
#     p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
#                                  universal_newlines=True)
#     for stdout_line in iter(p.stdout.readline, ''):
#         f.write(stdout_line.encode('utf-8'))
#
#     return p.communicate(f'{password}\n')


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
        backup('127.0.0.1', 'test', 'postgres', 'admin')
        print('ok')
    return app


if __name__ == '__main__':
    app = get_app()
    app.run(debug=True)