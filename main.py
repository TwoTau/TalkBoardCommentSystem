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
        template = JINJA_ENVIRONMENT.get_template('lecture-student-view.html')
        self.response.write(template.render({
            "token": rand(1000000, 9999999)
        }))

# /send
class ReceiveMessage(webapp2.RequestHandler):
    def post(self):
        now = (datetime.now()).strftime("%x %I:%M:%S %p")
        chat.append({
            "username": self.request.get("username"),
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
