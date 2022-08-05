from flask import render_template, request, Blueprint, redirect
from models.clients import ClientModel

submit_view = Blueprint('submit', __name__, template_folder='templates')


@submit_view.route('/u-had-submitted', methods=["POST", "GET"])
def submit():
    fname = request.form['fname']
    lname = request.form['lname']

    if fname and lname:
        client = ClientModel(fname, lname)
        client.add_client()
        return render_template("submit-success.html", data=fname)
    else:
        return render_template("submit-fail.html")