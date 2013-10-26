from flask import render_template, request
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = 'Hey girl hey', msg = 'Hello World')

@app.route('/login')
def login():
	login_user()
	return request.form

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/map')
def map():
	return render_template('map.html')


# @app.route('/hangout/new')
# def new_hangout():
# 	if request.method != 'POST'
# 		return render_template('')

# 	else
# 		create_new_hangout()
# 		return redirect(url_for('index'))

def create_new_hangout():
	return 'u'

def login_user():
	return 'u'

def logout_user():
	return 'u'

# get / (index)
# 	- if not logged in
# 		=> prompt login (facebook)
# 	- elif logged in && !avail
# 		=> create hangout?
# 		=> be available so your friends can hangout? (fomo fomo fomo)
# 	- else (logged in & available)
# 		=> (n friends are available, ) create a hangout?


# post /login
# 	- receive fb info
# 	- if new user
# 		=> persist in db
# 		=> get friend list & create friend associations w/ registered users
# 	- else
# 		=> update any change data

# 	save session (so they don't have to login again)

# 	redirect to index


# post /logout
# 	clear session



# get /hangout/new # create a new thing, and choose an activity/location
# post /hangout/new # process the new thing that this is

# get /hangout/{{id}} # show the hangout

# get /hangout/{{id}}/available_friends # list friends within radius of hangout location

# post /hangout/{{id}}/propose_alternative <-- i'm a responder and i don't like your activity?

# get /hangout/{{id}}/edit # change details and try to reinvite

# post /hangout/{{id}}/invite