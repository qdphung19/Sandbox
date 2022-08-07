from flask import render_template, Blueprint

index_view = Blueprint('index', __name__, template_folder='templates')

@index_view.route("/")
# @index_view.route("/index")
def index():
    return render_template("index.html")

