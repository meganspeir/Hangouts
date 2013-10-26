from app import db
ROLE_USER = 0
ROLE_ADMIN = 1

friends = db.Table('friends',
    db.Column('friend_id_one', db.Integer, db.ForeignKey('user.id')),
    db.Column('friend_id_two', db.Integer, db.ForeignKey('user.id'))
)

participants = db.Table('participants',
    db.Column('hangout', db.Integer, db.ForeignKey('hangout.id')),
    db.Column('participant', db.Integer, db.ForeignKey('user.id'))
)

class User(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(64), index = True, unique = True)
   phone_number = db.Column(db.Integer, index = True, unique = True)
   photo_url = db.Column(db.String(220))
   is_active = db.Column(db.Boolean)
   role = db.Column(db.SmallInteger, default = ROLE_USER)
   fb_access_token = db.Column(db.String(64), index = True, unique = True)
   fb_login_status = db.Column(db.Boolean)
   friend_linked = db.relationship('User',
        secondary = friends,
        primaryjoin = (friends.c.friend_id_one == id),
        secondaryjoin = (friends.c.friend_id_two == id),
        backref = db.backref('friends', lazy = 'dynamic'),
        lazy = 'dynamic')

   def __repr__(self):
       return '<User: name = %r, id = %r, is_active = %r>' % (self.name, self.id self.is_active)

class Hangout(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    creator = db.Column(db.Integer, db.ForeignKey('user.id'))
    location = db.Column(db.String(128), index = True)
    description = db.Column(db.String(256))
    type = db.Column(db.String(64), index = True)   # drink, eat, sing, etc
    last_request_time = db.Column(db.DateTime)
    request_count = db.Column(db.Integer)
    invited = db.relationship('Hangout',
        secondary = participants,
        primaryjoin = (participants.c.hangout == id),
        backref = db.backref('participants', lazy = 'dynamic'),
        lazy = 'dynamic')

    def __repr__(self):
       return '<Hangout: description = %r, id = %r, creator id = %r>' % (self.description, self.id, self.creator)
