# from fbchat import Client, log
# from fbchat.models import User
# from fbchat.models import *
# import json
# import os
#
# file_name = "session.json"
#
# with open(file_name) as f:
#     session = json.load(f)
# client = Client('hlhtstld307@gmail.com', '01652162621Trung', session_cookies=session)
# user = User("100014564863969")
# user_info = client.fetchUserInfo("100014564863969")["100014564863969"]

# from win32gui import PumpMessages
#
# PumpMessages()
# from selenium import webdriver

import zroya
import time


def send_message(nid, action_id):
    print('Sent')


zroya.init('Python', 'a', 'b', 'c', 'd')
t = zroya.Template(zroya.TemplateType.ImageAndText4)
t.setFirstLine('Hello My Friends')
t.setImage('F:\\LapTrinh\\Python code\\fb_mess_noti\\iconfinder_facebook_313103.ico')
t.addAction("Send")
zroya.show(t, on_action=send_message)
time.sleep(10)
