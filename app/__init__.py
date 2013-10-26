from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment
from webassets.loaders import PythonLoader

app = Flask(__name__)
assets = Environment(app)


# Config
app.config.from_object('config')


# Load and register assets bundles.
# bundles = PythonLoader('bundles').load_bundles()

# for name, bundle in bundles.iteritems():
#     assets.register(name, bundle)


# Db
db = SQLAlchemy(app)


# MVC
from app import views, models
