from flask import Flask, render_template, request, redirect, url_for
from flask_login import login_user, login_required, LoginManager
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)
database = SQLAlchemy(app)

from db import models


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/profile')
@login_required
def profile():
    continents = models.Continent.query.all()
    countries = models.Country.query.all()
    return render_template('profile.html', continents=continents, countries=countries)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/sign_in', methods=["POST"])
def sign_in():
    login_field = request.form.get('login')
    password = request.form.get('password')

    user = models.User.query.filter_by(
        login=login_field, password=password).first()
    if not user or not user.password == password:
        return redirect(url_for('index'))

    login_user(user)
    return redirect(url_for('profile'))


if __name__ == '__main__':
    app.run()
