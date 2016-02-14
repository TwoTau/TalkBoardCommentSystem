"""`main` is the top level module for your Flask application."""

import jinja2
import os
import webapp2

from random import randint as rand

from datetime import datetime

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

chat = []

# /
class MainPage(webapp2.RequestHandler):
    def get(self):
        token = rand(1000000, 9999999)
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({
            "randomNumber": rand(100, 999),
            "token": token
        }))

# /send
class ReceiveMessage(webapp2.RequestHandler):
    def post(self):
        now = (datetime.now()).strftime("%x %I:%M:%S %p")
        chat.append({
            "username": self.request.get("username"),
            "parentId": self.request.get("parentMessage"),
            "date": now,
            "content": self.request.get("message")
        });

# /messages
class SendHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('messages.html')
        self.response.write(template.render({
            "chatList": chat
        }))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/send', ReceiveMessage),
    ('/messages', SendHandler)
], debug=True)
