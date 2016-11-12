from handlers import *

#TODO's found in handlers/base.py :)
#This class contains all the routes and runs the web app, and contains the accessable handlers.
#These handles correspond with the accessable routes available to the public, as defined in the handlers/base.py file
#All handlers are found in the /handlers folder, and all the corresponding templates are there as well.
#See the base.py file in handlers for more information.

#Temporary, only for hosting on github pages at the moment
class IndexHandler(base.Utilities):
    def get(self):
        t = base.jinja_env.get_template("index.html")
        response = t.render();
        self.response.write(response)


class HomepageHandler(base.Utilities):
    def get(self):
        if not self.user:
            t = base.jinja_env.get_template("homepage_lgfalse.html")
            response = t.render()
            self.response.write(response)
        else:
            t = base.jinja_env.get_template("homepage_lgtrue.html")
            response = t.render(username = self.user.username)
            self.response.write(response)

"""class AboutHandler(base.Utilities):

#Shows references and resources used
class ResourceHandler(base.Utilities):

class ProfileHandler(base.Utilities):
    def get(self):
        t = jinja_

"""

app = base.webapp2.WSGIApplication([
    #General pages
    ("/", IndexHandler),
    ('/homepage', HomepageHandler),
    ('/signup', authenticationHandlers.SignupHandler),
    ('/login', authenticationHandlers.LoginHandler),
    ('/logout', authenticationHandlers.LogoutHandler),
    #User pages
    #base.webapp2.Route('/profile/<username:[a-zA-Z0-9_-]{8,20}',ProfileHandler) #TODO: Implement this

], debug=True)
