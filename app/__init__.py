from flask import Flask
from flask.ext.assets import Environment
from webassets.loaders import PythonLoader
from database import db_session

app = Flask(__name__)
assets = Environment(app)


app.config.from_object('config')


# Load and register assets bundles.
bundles = PythonLoader('bundles').load_bundles()
for name, bundle in bundles.iteritems():
    assets.register(name, bundle)



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


import app.views
