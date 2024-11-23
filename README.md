# Django-Polls

Um projeto vindo da documentação do Django 5.1.3, enquanto vou aprofundando meus conhecimentos neste framework

## Estrtura do projeto

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
