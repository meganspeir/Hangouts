from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = 'Hey girl hey', msg = 'Hello World')

# Facebook login redirect url
# Save the user if new?
def login():


