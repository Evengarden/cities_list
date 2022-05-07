Установка зависимостей
---
    $ pip install -r requirements.txt
---

Оставил файлы окружения намеренно.


База данных
---
    $ python manage.py db init - запустить сидер
    $ python manage.py db migrate 
    $ python manage.py db upgrade - обновление моделей данных
    $ python manage.py seed - запустить сидер
---

Запуск
---
    $export APP_SETTINGS=config.DevelopmentConfig
    $flask run
---