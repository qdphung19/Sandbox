from flask import render_template, Blueprint, redirect, flash, url_for
from form import LoginForm

login_view = Blueprint('login', __name__, template_folder='templates')

@login_view.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Demand log-in de user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('submit.submit'))
    return render_template('login.html', title='Sign In', form=form)