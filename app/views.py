from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from werkzeug.datastructures import ImmutableMultiDict
from app import app, models
from database import db_session
    
@app.route('/')
@app.route('/index')
def index(): # get post
    # return render_template('index.html', title='Hey', msg='Foo')
	# session['user'] = user first and last name
    if session.get('user', -1) == -1:
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
        print "postttt"

        # if there's a user id & no db user => create
        if userID:
            print "i can hz id"
            print userID

            user = models.User.query.get(userID)

            print 'i got past the querying'
            print user

            if not user:
                print "I DON'T EXIST ;_____;"

                print request.form['userID']

                print 'req form'

                # print request.form['user']
                baseObject = ImmutableMultiDict(request.form)

                # userObj = baseObject.getlist('user')
                print 'name?'
                print baseObject.get('name')
                # print userObj

                # raise IOError

                user = models.User(id = userID, name = baseObject.get('name'), role = 0, fb_access_token = request.form['accessToken'])

                # Find any existing users in our db who are in this person's friend list


                db_session.add(user)
                db_session.commit()
                return jsonify({'success': True}), 200
            else:
                print "i exist?"
                return jsonify({'success': True}), 200


        # there's no userId in the request
        else:
            return redirect(url_for('index'))
        

	return "something"

@app.route('/success')
def success():
    return 'you win at life'

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
            # pass
        # elif not description:
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
