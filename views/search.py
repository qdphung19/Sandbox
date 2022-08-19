from flask import render_template, request, Blueprint, redirect, flash
# from models.clients_test import ClientTest

search_view = Blueprint('search', __name__, template_folder='templates')

@search_view.route('/search')
def search():
    kw = request.args.get("keyword")
    # print(kw)

    # client_list = ClientTest.dbmongo_find(kw)

    return render_template("search.html", client_list = client_list)