from flask import render_template, request
from app import app

    
@app.route('/')
@app.route('/index')
def index(): # get post
    if !session['user']:
        pass #=> prompt login (facebook)
    elif session['user'] && !session['available']:
        pass
# 		=> create hangout?
# 		=> be available so your friends can hangout? (fomo fomo fomo)
    else:
        pass
# 		=> (n friends are available, ) create a hangout?


@app.route('/login')
def login():
	return request.form
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