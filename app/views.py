from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from app import app, models
    
@app.route('/')
@app.route('/index')
def index(): # get post
    return render_template('index.html', title='Hey', msg='Foo')
	# session['user'] = user first and last name
    if not session['user']:
        #=> prompt login (facebook)
        return render_template('index.html', title='Hey', msg='Foo')
        # session['available'] = on or off

    elif session['user'] and not session['available']:
        pass
		# 		=> create hangout?
		# 		=> be available so your friends can hangout? (fomo fomo fomo)
    else: #session['user'] && session['available']
        pass
		# 		=> (n friends are available, ) create a hangout?


@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/store_location', methods = ['POST', 'PUT'])
def store_location():
    locations = {}

    for key in ['latitude', 'longitude']:
        # locations[request.form.id]
        locations[key] = request.form[key]

    return jsonify(locations), 200



@app.route('/login', methods=['GET', 'POST']) # post
def login():
    error = None
    if request.method == 'POST':
        userID = request.form['userID']

        # if there's a user id & no db user => create
        if userID:
            userObj = request.form['user']

            user = models.User.query.get(userID)

            # if not user
            #     user = models.User(id = userId, name = user['name'], photo_url = user['picture'], role = 0, fb_access_token = request.form['accessToken'])
            #     db.session.add(user)
            #     db.session.commit()


        # there's no userId in the request
        else:
            return redirect(url_for('index'))
        
    # 	- receive fb info
    # 	- if new user
    # 		=> persist in db
    # 		=> get friend list & create friend associations w/ registered users
    # 	- else
    # 		=> update any change data


    # 	save session (so they don't have to login again)

    # 	redirect to index
	return request.form

@app.route('/users')
def users():
    users = models.User.query.all()

    str = ""
    for user in users:
        str += user.name 

    return str

@app.route('/logout')
def logout(): # post
    session.clear()
    return redirect(url_for("index"))


@app.route('/hangout/new')
def create_hangout():
    hangout = False
    while not hangout:
        if not location_map:
            #show map
            pass
        elif not hangout_type:
            #render pull down list with suggestions of hangout categories
            pass
        elif not description:
            #render a text box to submit description of hangout
            pass
        elif not friends:
            #render alert about which friends (pull down list with suggestions of hangout categories)
            pass
        else:
            # post hangout to DB
            # ping friends in hangout
            hangout = True
            return redirect('/hangout/{{id}}')

@app.route('/hangout/{{id}}')
# get /hangout/{{id}} # show the hangout

@app.route('/hangout/{{id}}/propose_alternative')
def change_hangout():
    hangout = False
    while not hangout:
        if not location_map:
            #show map
            pass
        elif not hangout_type:
            #render pull down list with suggestions of hangout categories
            pass
        elif not description:
            #render a text box to submit description of hangout
            pass
        else:
            # post hangout to DB
            # ping friends in hangout
            hangout = True
            return redirect('/hangout/{{id}}')

# get /hangout/{{id}}/edit # change details and try to reinvite
@app.route('/hangout/{{id}}/edit')
def edit_hangout():
    hangout = False
    while not hangout:
        if not location_map:
            #show map
            pass
        elif not hangout_type:
            #render pull down list with suggestions of hangout categories
            pass
        elif not description:
            #render a text box to submit description of hangout
            pass
        elif not friends:
            #render alert about which friends (pull down list with suggestions of hangout categories)
            pass
        else:
            # post hangout to DB
            # ping friends in hangout
            hangout = True
            return redirect('/hangout/{{id}}')



# post /hangout/{{id}}/invite

