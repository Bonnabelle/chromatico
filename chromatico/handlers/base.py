#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#This is the base template for all the handlers to inherit from

#Top-level imports
import webapp2, jinja2, os
from models import User, UserStats
from util import * #Imports the security/misc. utilities needed to authenticate users and hash things.
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

#TODO: Handler for the homepage (make sure to show a few more features for those logged in) OWATTA
#TODO: Handler for signup then followed  by the quiz, show results, score results in DB, then when the user is ready, redirect to user profile
#TODO: Handler for user profile
#TODO: Handler for each level ugGggGgHh THIS COULD CHANGE, WILL NEED TO DO MORE RESEARCH!!!!!
#TODO: Handlers for the final tests for each level.
#TODO: Once someone reaches level 4, they have access to make quizzes of their own with songs and snippets, etc. A kind of quiz building tool.
#TODO: Handler for user quiz/training.

accessable = [
    '/homepage','/about','/resources','/login','/signup'
]

errors = {}

class Utilities(webapp2.RequestHandler):

    def get_user_info(self, username):
        user = db.GqlQuery("SELECT * FROM User WHERE username = '%s'" % username)
        if user:
            return user.get()
        else:
            return False

    def login_user(self, user):
        user_id = user.key().id()
        self.set_secure_cookie('user_id', str(user_id))

    def logout_user(self):
        """ Logout a user specified by a User object user """
        self.set_secure_cookie('user_id', '')

    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        if cookie_val:
            return hashutils.check_secure_val(cookie_val)

    def set_secure_cookie(self, name, val):
        cookie_val = hashutils.make_secure_val(val)
        self.response.headers.add_header('Set-Cookie', '%s=%s; Path=/' % (name, cookie_val))

    def initialize(self, *a, **kw):
        #Limits where a user can go if they're not logged in, based on the accessable paths specified below.
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie('user_id')
        self.user = uid and User.get_by_id(int(uid))

        if not self.request.path in accessable:
            self.redirect('/login')
