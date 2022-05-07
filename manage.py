import os
import data_dict
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from db.models import Continent, Country, User, City

from app import app, database

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, database)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def seed():
    continents = [Continent('Азия'), Continent('Америка'), Continent('Африка'),
                  Continent('Европа')]

    for obj in continents:
        database.session.add(obj)

    countries = [Country('Япония', 1), Country('Индонезия', 1), Country('Индия', 1),
                 Country('Филлипины', 1), Country('Китай', 1), Country('США', 2),
                 Country('Бразилия', 2), Country('Мексика', 2), Country('Аргентина', 2),
                 Country('Перу', 2), Country('Египет', 3), Country('Нигерия', 3),
                 Country('Конго', 3), Country('ЮАР', 3), Country('Ангола', 3),
                 Country('Кения', 3), Country('Танзания', 3), Country('Россия', 4),
                 Country('Турция', 4), Country('Франция', 4), Country('Великобритания', 4),
                 Country('Испания', 4), Country('Италия', 4)]

    for obj in countries:
        database.session.add(obj)

    cities = [City('Токио', data_dict.cities['Токио'][1], data_dict.cities['Токио'][0]),
              City('Джакарта', data_dict.cities['Джакарта'][1], data_dict.cities['Джакарта'][0]),
              City('Дели', data_dict.cities['Дели'][1], data_dict.cities['Дели'][0]),
              City('Манила', data_dict.cities['Манила'][1], data_dict.cities['Манила'][0]),
              City('Шанхай', data_dict.cities['Шанхай'][1], data_dict.cities['Шанхай'][0]),
              City('Мумбаи', data_dict.cities['Мумбаи'][1], data_dict.cities['Мумбаи'][0]),
              City('Пекин', data_dict.cities['Пекин'][1], data_dict.cities['Пекин'][0]),
              City('Гуанчжоу', data_dict.cities['Гуанчжоу'][1], data_dict.cities['Гуанчжоу'][0]),
              City('Осака', data_dict.cities['Осака'][1], data_dict.cities['Осака'][0]),
              City('Нью-Йорк', data_dict.cities['Нью-Йорк'][1], data_dict.cities['Нью-Йорк'][0]),
              City('Сан-Пауло', data_dict.cities['Сан-Пауло'][1], data_dict.cities['Сан-Пауло'][0]),
              City('Мехико', data_dict.cities['Мехико'][1], data_dict.cities['Мехико'][0]),
              City('Лос-Анджелес', data_dict.cities['Лос-Анджелес'][1], data_dict.cities['Лос-Анджелес'][0]),
              City('Буэнос-Айрес', data_dict.cities['Буэнос-Айрес'][1], data_dict.cities['Буэнос-Айрес'][0]),
              City('Лима', data_dict.cities['Лима'][1], data_dict.cities['Лима'][0]),
              City('Чикаго', data_dict.cities['Чикаго'][1], data_dict.cities['Чикаго'][0]),
              City('Даллас', data_dict.cities['Даллас'][1], data_dict.cities['Даллас'][0]),
              City('Сан-Хосе', data_dict.cities['Сан-Хосе'][1], data_dict.cities['Сан-Хосе'][0]),
              City('Каир', data_dict.cities['Каир'][1], data_dict.cities['Каир'][0]),
              City('Лагос', data_dict.cities['Лагос'][1], data_dict.cities['Лагос'][0]),
              City('Киншаса', data_dict.cities['Киншаса'][1], data_dict.cities['Киншаса'][0]),
              City('Йоханнесбург', data_dict.cities['Йоханнесбург'][1], data_dict.cities['Йоханнесбург'][0]),
              City('Луанда', data_dict.cities['Луанда'][1], data_dict.cities['Луанда'][0]),
              City('Найроби', data_dict.cities['Найроби'][1], data_dict.cities['Найроби'][0]),
              City('Дар-эс-Салам', data_dict.cities['Дар-эс-Салам'][1], data_dict.cities['Дар-эс-Салам'][0]),
              City('Александрия', data_dict.cities['Александрия'][1], data_dict.cities['Александрия'][0]),
              City('Москва', data_dict.cities['Москва'][1], data_dict.cities['Москва'][0]),
              City('Стамбул', data_dict.cities['Стамбул'][1], data_dict.cities['Стамбул'][0]),
              City('Париж', data_dict.cities['Париж'][1], data_dict.cities['Париж'][0]),
              City('Лондон', data_dict.cities['Лондон'][1], data_dict.cities['Лондон'][0]),
              City('Мадрид', data_dict.cities['Мадрид'][1], data_dict.cities['Мадрид'][0]),
              City('Милан', data_dict.cities['Милан'][1], data_dict.cities['Милан'][0]),
              City('Санкт-Петербург', data_dict.cities['Санкт-Петербург'][1],
                   data_dict.cities['Санкт-Петербург'][0]),
              City('Анкара', data_dict.cities['Анкара'][1], data_dict.cities['Анкара'][0]),
              City('Барселона', data_dict.cities['Барселона'][1], data_dict.cities['Барселона'][0]), ]

    for obj in cities:
        database.session.add(obj)

    users = [User('test', 'test'), User('test2', 'test2')]
    for obj in users:
        database.session.add(obj)

    database.session.commit()


if __name__ == '__main__':
    manager.run()
