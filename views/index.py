from flask import render_template, Blueprint
from __init__ import get_app

index_view = Blueprint('index', __name__, template_folder='templates')


@index_view.route("/")
def index():
    return render_template("index.html")

