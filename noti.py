from win10toast import ToastNotifier
from fbchat import Client, log
from fbchat.models import *
import json
import os
import webbrowser
from datetime import datetime
from selenium import webdriver

DISCONNECTED_MSG = 'Unable to evaluate script: disconnected: not connected to DevTools\n'
ICON_PATH = "F:\\LapTrinh\\Python code\\fb_mess_noti\\iconfinder_facebook_313103.ico"
toaster = ToastNotifier()

class fb_noti(Client):

    def onInbox(self, unseen=None, unread=None, recent_unread=None, msg=None):
        log.info('Inbox event: Chưa xem: {}, Chưa đọc: {}, Chưa đọc gần đây: {}'.format(unseen, unread, recent_unread))

    def open_browser(self):
        try:
            # chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            # webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path), 1)
            # controller = webbrowser.get('chrome')
            # controller.open_new_tab('facebook.com')
            self.driver = webdriver.Chrome()
            self.driver.get("https://www.facebook.com")
        except Exception as e:
            print('error')
            return

    def onMessage(self, mid=None, author_id=None, message=None,  message_object=None, thread_id=None,
                  thread_type=ThreadType.USER, ts=None, metadata=None, msg={}):
        if author_id == self.uid:
            return
        user_info = self.fetchUserInfo(author_id)[author_id]
        log.info('Nhận được tin nhắn từ {} với nội dung là: {}'.format(user_info.nickname or user_info.own_nickname or user_info.name, message))
        if message is None:
            message = "None"
        if message == "":
            message = "Sticker or something else"
        if author_id == "100006639668573":
            if self.driver.get_log('driver')[-1]['message'] != DISCONNECTED_MSG:
                toaster.show_toast("Notification {}".format(user_info.nickname or user_info.own_nickname or user_info.name),
                                                            message,
                                                            icon_path=ICON_PATH,
                                                            callback_on_click=self.open_browser)

    def onMessageSeen(self, seen_by=None, thread_id=None, thread_type=ThreadType.USER, seen_ts=None, ts=None, metadata=None, msg=None):
        user_info = self.fetchUserInfo(seen_by)[seen_by]
        log.info('Tin nhắn đã được xem bởi {} trong {} vào lúc {}'.format(user_info.nickname or user_info.own_nickname or user_info.name,
                                                                          thread_type,
                                                                          datetime.now()))

    def onMessageDelivered(self, msg_ids=None, delivered_for=None, thread_id=None, thread_type=ThreadType.USER, ts=None, metadata=None, msg=None):
        user_info = self.fetchUserInfo(delivered_for)[delivered_for]
        log.info("Tin nhắn {} đã được gửi tới {} ({}) vào lúc {}s".format(msg_ids,
                                                                          user_info.nickname or user_info.own_nickname or user_info.name,
                                                                          thread_id, thread_type.name,
                                                                          ts / 1000))

file_name = "session.json"
client = None

try:
    with open(file_name, 'r') as f:
        session = json.load(f)
except Exception as e:
    pass

client = fb_noti('hlhtstld307@gmail.com', '01652162621Trung', session_cookies=session)

client.listen()
# unreads = client.fetchUnread()
# print(len(unreads))
# for unread in unreads:
#     print(unread)
#     # Gets the last 10 messages sent to the thread
#     messages = client.fetchThreadMessages(thread_id=unread, limit=10)
#     # Since the message come in reversed order, reverse them
#     messages.reverse()
#     # Prints the content of all the messages
#     for message in messages:
#         print(message.text)

session = client.getSession()
with open(file_name, 'w') as outfile:
    json.dump(session, outfile)
