from app import database, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def get_user(ident):
    return User.query.get(int(ident))


class User(database.Model, UserMixin):
    __tablename__ = 'users'
    id = database.Column(database.Integer, primary_key=True)
    login = database.Column(database.String(), unique=True)
    password = database.Column(database.String())

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Continent(database.Model):
    __tablename__ = 'continents'
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(256))
    countries = database.relationship('Country', backref='continent', lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Country(database.Model):
    __tablename__ = 'countries'
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(256))
    continent_id = database.Column(database.Integer, database.ForeignKey('continents.id'))
    cities = database.relationship('City', backref='country', lazy=True)

    def __init__(self, name, continent_id):
        self.name = name
        self.continent_id = continent_id

    def __repr__(self):
        return '<id {}>'.format(self.id)


class City(database.Model):
    __tablename__ = 'cities'
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(256))
    population = database.Column(database.Integer)
    country_id = database.Column(database.Integer, database.ForeignKey('countries.id'))

    def __init__(self, name, population, country_id):
        self.name = name
        self.population = population
        self.country_id = country_id

    def __repr__(self):
        return '<id {}>'.format(self.id)
