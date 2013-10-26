from sqlalchemy import Column, Integer, String, Boolean, DateTime, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

ROLE_USER = 0
ROLE_ADMIN = 1

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    name = Column(String(64), index = True, unique = True)
    phone_number = Column(String(16), index = True, unique = True)
    photo_url = Column(String(220))
    is_active = Column(Boolean)
    role = Column(SmallInteger, default = ROLE_USER)
    fb_access_token = Column(String(64), index = True, unique = True)
    fb_login_status = Column(Boolean)

    def __repr__(self):
        return '<User: name = %r, id = %r>' % (self.name, self.id)

class Hangout(Base):
    __tablename__ = 'hangout'

    id = Column(Integer, primary_key = True)
    creator_id = Column(Integer, ForeignKey('user.id'))
    location = Column(String(128), index = True)
    description = Column(String(256))
    type = Column(String(64), index = True)   # drink, eat, sing, etc
    last_request_time = Column(DateTime)
    request_count = Column(Integer)

    def __repr__(self):
        return '<Hangout: description = %r, id = %r, creator id = %r>' % (self.description, self.id, self.creator_id)

class Friend(Base):
    __tablename__ = 'friend'

    id = Column(Integer, primary_key = True)
    friend_one_id = Column(Integer, ForeignKey('user.id'))
    friend_two_id = Column(Integer, ForeignKey('user.id'))

    friend_one = relationship(User, primaryjoin=User.id == friend_one_id)
    friend_two = relationship(User, primaryjoin=User.id == friend_two_id)

    def __repr__(self):
        return '<Friend: friend_one_id = %r, friend_two_id = %r>' % (self.friend_one_id, self.friend_two_id)

class Participant(Base):
    __tablename__ = 'participant'

    id = Column(Integer, primary_key = True)
    hangout_id = Column(Integer, ForeignKey('hangout.id'))
    participant_id = Column(Integer, ForeignKey('user.id'))

    hangout = relationship(Hangout, primaryjoin=Hangout.id == hangout_id)
    participant = relationship(User, primaryjoin=User.id == participant_id)

    def __repr__(self):
        return '<Participant: hangout_id = %r, participant_id = %r>' % (self.hangout_id, self.participant_id)
