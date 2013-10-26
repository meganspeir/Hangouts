from app import models
from database import db_session
import datetime

u1 = models.User(name = "Sharon",
    phone_number = "415-555-1234",
    photo_url = "https://pbs.twimg.com/profile_images/2032784664/sharon-on-a-bike.jpg",
    is_active = True,
    fb_access_token = "fake_token_1",
    fb_login_status = True)

u2 = models.User(name = "Megan",
    phone_number = "415-555-1235",
    photo_url = "https://pbs.twimg.com/profile_images/378800000412738531/c224de0963f9012e5ce14aaec9908726.jpeg",
    is_active = True,
    fb_access_token = "fake_token_2",
    fb_login_status = True)

u3 = models.User(name = "Kara",
    phone_number = "415-555-1236",
    photo_url = "https://pbs.twimg.com/profile_images/378800000518638183/d5741ff83e09f5b5f4638ee4000e4ee5.jpeg",
    is_active = True,
    fb_access_token = "fake_token_3",
    fb_login_status = True)

u4 = models.User(name = "Ni",
    phone_number = "415-555-1237",
    photo_url = "https://pbs.twimg.com/profile_images/378800000393956742/b52d80325c880c06288eac93b4aa321e.jpeg",
    is_active = True,
    fb_access_token = "fake_token_4",
    fb_login_status = True)

u5 = models.User(name = "Ingrid",
    phone_number = "415-555-1238",
    photo_url = "https://pbs.twimg.com/profile_images/378800000574530232/2082ef286492c586e7e2e37c5457c50a.jpeg",
    is_active = True,
    fb_access_token = "fake_token_5",
    fb_login_status = True)

user_list = [u1, u2, u3, u4, u5]
db_session.add_all(user_list)

f1 = models.Friend(friend_one_id = 2, friend_two_id = 1)
f2 = models.Friend(friend_one_id = 2, friend_two_id = 3)
f3 = models.Friend(friend_one_id = 2, friend_two_id = 4)
f4 = models.Friend(friend_one_id = 2, friend_two_id = 5)

friends_list = [f1, f2, f3, f4]
db_session.add_all(friends_list)

h1 = models.Hangout(creator_id = 2,
    location = "YamaSho",
    description = "Friday night karaoke!!",
    type = "singing",
    last_request_time = datetime.datetime.now(),
    request_count = 1)
db_session.add(h1)

i1 = models.Participant(hangout_id = 1, participant_id = 1)
i2 = models.Participant(hangout_id = 1, participant_id = 3)
i3 = models.Participant(hangout_id = 1, participant_id = 4)
i4 = models.Participant(hangout_id = 1, participant_id = 5)

invitation_list = [i1, i2, i3, i4]
db_session.add_all(invitation_list)

db_session.commit()
