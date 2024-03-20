# TODO: Implement Routing
from application import app, db
from flask import request, flash, redirect, url_for, render_template
from flask_login import login_required, login_user
from application.forms import LoginForm
from application.models import SiteAdmin
from application import login_manager
from datetime import timedelta

login_manager.login_view = "login"

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def homepage():
    ...

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = db.session.get(SiteAdmin, form.user_id.data)
        login_user(user, remember=True, duration=timedelta(minutes=10))

        flash('Logged in successfully.')

        next = request.args.get('next')
        # url_has_allowed_host_and_scheme should check if the url is safe
        # for redirects, meaning it matches the request host.
        # See Django's url_has_allowed_host_and_scheme for an example.
        # if not url_has_allowed_host_and_scheme(next, request.host):
        #     return flask.abort(400)

        return redirect(next or url_for('index'))
    return render_template('login.html', form=form)

@app.route('employee-details', methods=['GET'])
@login_required
def get_employees():
    return "WORKING"