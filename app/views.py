from flask import render_template, request
from app import app

    
@app.route('/')
@app.route('/index')
def index(): # get post
	# session['user'] = user first and last name
    if !session['user']:
        #=> prompt login (facebook)
        return render_template("index.html")
# session['available'] = on or off

    elif session['user'] && !session['available']:
        pass
		# 		=> create hangout?
		# 		=> be available so your friends can hangout? (fomo fomo fomo)
    else: #session['user'] && session['available']
        pass
		# 		=> (n friends are available, ) create a hangout?


@app.route('/login') # post
def login():
# 	- receive fb info
# 	- if new user
# 		=> persist in db
# 		=> get friend list & create friend associations w/ registered users
# 	- else
# 		=> update any change data


# 	save session (so they don't have to login again)

# 	redirect to index
	return request.form


@app.route('/logout')
def logout(): # post
    session.clear()
    return redirect(url_for("index"))


@app.route('/hangout/new')
def create_hangout():
    hangout = False
    while !hangout:
        if !location_map:
            #show map
            pass
        elif !hangout_type:
            #render pull down list with suggestions of hangout categories
            pass
        elif !description:
            #render a text box to submit description of hangout
            pass
        elif !friends:
            #render alert about which friends (pull down list with suggestions of hangout categories)
            pass
        else:
            # post hangout to DB
            # ping friends in hangout
            hangout = True
            return redirect('/hangout/{{id}}')

@app.route('/hangout/{{id}}')
# get /hangout/{{id}} # show the hangout

# get /hangout/{{id}}/available_friends # list friends within radius of hangout location

# post /hangout/{{id}}/propose_alternative <-- i'm a responder and i don't like your activity?

# get /hangout/{{id}}/edit # change details and try to reinvite

# post /hangout/{{id}}/invite

if __name__ == "__main__":
    app.run(debug = True)
