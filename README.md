
# django-polls

## django-polls is a Django app to conduct web-based polls. For each question, visitors can choose between a fixed number of answers. Detailed documentation is in the "docs" directory

## Quick start

1. Add "polls" to your INSTALLED_APPS setting like this::
INSTALLED_APPS = [
...,
"django_polls",
]
2. Include the polls URLconf in your project urls.py like this::
path("polls/", include("django_polls.urls")),
3. Run ``python manage.py migrate`` to create the models.
4. Start the development server and visit the admin to create a poll.
5. Visit the ``/polls/`` URL to participate in the poll.

## project tree

```Django Pools Tree
Django-Pools/
    ├── README.md
    ├── poetry.lock
    ├── project/
    │   ├── apps/
    │   │   ├── __init__.py
    │   │   └── polls/
    │   │       ├── __init__.py
    │   │       ├── admin.py
    │   │       ├── apps.py
    │   │       ├── migrations/
    │   │       ├── models.py
    │   │       ├── urls.py
    │   │       └── views.py
    │   ├── database/
    │   │   └── db.sqlite3
    │   ├── manage.py
    │   ├── server/
    │   │   ├── __init__.py
    │   │   ├── asgi.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   └── wsgi.py
    │   ├── static/
    │   │   ├── css/
    │   │   │   └── style.css
    │   │   └── js/
    │   │       └── main.js
    │   └── templates/
    │       ├── layout.html
    │       └── polls/
    │           ├── detail.html
    │           ├── index.html
    │           └── results.html
    ├── pyproject.toml
    ├── settings.yaml
    └── tests/
        └── polls/
            └── test_model.py
```

## Executar teste no Django

Como mostrado na arvore do projeto, a tasta `test/` está localizada na pasta raiz do projeto, para isso use o comando

`python project/manage.py test tests/polls`
