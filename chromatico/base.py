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

#CHROMATICO - Final project #1 using Python 2/3 HTML + CSS and JavaScript



#This is the base template for all the handlers to inherit from

#Top-level imports
import webapp2, jinja2, os,sys
from models import *
from util import * #Imports the security/misc. utilities needed to authenticate users and hash things.
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

sys.dont_write_bytecode = 1


#TODO: Once someone reaches level 4, they have access to the number/note fusion tool, allowing them to input numbers and there would be
#      a mp3 audio output that mashed them all together according to 4/4 comon time

accessable = [
    '/','/homepage','/about','/resources','/login','/signup'
]
users = 0
visits = 0

class Utilities(webapp2.RequestHandler):
    def get_user_info(self, username):
        user = db.GqlQuery("SELECT * FROM User WHERE username = '%s'" % username)
        if user:
            return user.get()

    def get_user_amount(self):
        users = db.GqlQuery("SELECT * FROM User")
        i = 0
        for u in users:
            i += 1
        return i

    def get_comments(self,author):
        comments = db.GqlQuery("SELECT * FROM Comments WHERE author = '%s'" % author)
        if comments:
            return comments

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
        self.current_user = uid and User.get_by_id(int(uid))
        self.users = self.get_user_amount()

        # If not a current user and they try to access the unaccessable
        if not self.current_user and self.request.path not in accessable:
            self.redirect('/login')

        elif self.current_user and self.request.path == '/login':
            self.redirect('/logout')
