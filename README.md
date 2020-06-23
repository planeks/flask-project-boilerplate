# Flask Project Boilerplate

This repository is a boilerplate Flask project for quickly getting started.

## Getting started

Steps:

1. Clone/pull/download this repository
2. Create a virtualenv with `python3 -m venv env_py37` and install dependencies with `pip install -r requirements.txt`
3. Rename `example.env` to `.env`
4. Configure your `.env` variables
5. Apply migrations with `python manage.py db upgrade`

## Basics

### How to run local development server

    python manage.py runserver
    
### How to initial migrations

    python manage.py db init
    
### How to make migrations

    python manage.py db migrate
    
### How to apply migrations

    python manage.py db upgrade
    
### How to downgrade migrations

    python manage.py db downgrade

### How to run unit tests

    python -m unittest
    
### How to add a new model

* Create a file of the model in `src/models` directory.

* Create the class of model and inheritance it from `(db.Model, BaseModel)` in the model file. Example:

```python
from src.model import db
from src.model.abc import BaseModel

class Cat(db.Model, BaseModel):
    __tablename__ = 'cat'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
```

* Add `from .cat import Cat` to the end of `src/model/__init__.py`

* Make migrations with `python manage.py db migrate`

* Apply migrations with `python manage.py db upgrade`

### How to create API entry point:

* Create the resource file in `src/resource` directory.

* Create a resource class in the resource file. Example:

```python
from flask_restful import Resource, abort

from src.model.cat import Cat

class CatAPI(Resource):
    def get(self, id):
        cat = Cat.query.get(id)
        if cat is None:
            abort(404)
        cat_dict = cat.json
        return cat_dict
```

* Create the route file in `src/roure` directory. And add routs:

```python
from flask import Blueprint
from flask_restful import Api


cat_blueprint = Blueprint('cat', __name__)
cat_blueprint_api = Api(cat_blueprint)


from src.resource.cat import CatAPI
cat_blueprint_api.add_resource(CatAPI, '/cat/<int:id>')
```

* Associate your blueprint with Flask app. Add 2 string to `src/server.py`:

```python
from src.route.cat import cat_blueprint
server.register_blueprint(cat_blueprint)
```