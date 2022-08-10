from flask import render_template, request, Blueprint, redirect, flash
from models.clients import ClientModel

submit_view = Blueprint('submit', __name__, template_folder='templates')


@submit_view.route('/submit', methods=["POST", "GET"])
def submit():
    fname = request.form.get('fname', False)
    lname = request.form.get('lname', False)

    # kw = request.args.get("keyword")
    # print(kw)

    client = ClientModel(fname, lname)
    # client_list = ClientModel.dbmongo_find(kw)


    if fname and lname:
        client.add_client()
        flash("successfully !!!")
        return render_template("submit.html", data=fname)
    else:
        flash("failed !")
        return render_template("submit.html")