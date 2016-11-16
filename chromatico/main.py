from base import *
import Quiz

#TODO's found in handlers/base.py :)
#NOTE: This class contains all the routes and runs the web app, and contains most of the handlers available to the public.
#These handles correspond with the accessable routes available to the public, as defined in the handlers/base.py file
#All handlers are found in the /handlers folder, and all the corresponding templates are there as well.
#See the base.py file in handlers for more information.


#Homepage
class HomepageHandler(Utilities):
    def get(self):
        self.response.out.write("Current user isn't working, its returning: " + str(current_user))
        """
        if not current_user:
            t = jinja_env.get_template("homepage_lgfalse.html")
            response = t.render()
            self.response.write(response)
        else:
            t = jinja_env.get_template("homepage_lgtrue.html")
            response = t.render(username = current_user.username)
            self.response.write(response)"""
#Resources
class ResourcesHandler(Utilities):
    def get(self):
        t = jinja_env.get_template("resources.html")
        response = t.render()
        self.response.write(response)

#Signup
class SignupHandler(Utilities):
    def get(self):
        t =  jinja_env.get_template("signup.html")
        response = t.render(errors = errors)
        self.response.write(response)

    def post(self):
        sub_user = self.request.get("username")
        sub_pass = self.request.get("password")
        sub_pass_ver = self.request.get("password_ver")
        sub_em = self.request.get("email")

        username = validations.validate_username(sub_user)
        pas = validations.validate_password(sub_pass)
        pas_ver = validations.validate_verify(sub_pass,sub_pass_ver)
        em = validations.validate_email(sub_em)

        if username != False and pas != False and pas_ver != False and sub_em != False:
            pw_hash = hashutils.make_pw_hash(username, pas)
            user = User(username=username, pw_hash=pw_hash, taken_assess = False, email = em)
            user.put()
            user_stats = UserStats(statistics_owner = user.username, quizzes_complete = 0, percentage_correct = 0.0, points = 0)
            user_stats.put()

            self.login_user(user)

            self.redirect('/s-signupq')
        else:
            error = True

            if username == False:
                errors ["ue"] = "Your username is invalid."

            if pas == False:
                errors ["pe"] = "Your password is invalid."

            if pas_ver == False:
                errors ["pve"] = "Your passwords don't match."

            if em == False:
                errors ["e_e"] = "Your email is invalid."

            t =  jinja_env.get_template("signup.html")
            response = t.render(errors=errors)
            self.response.write(response)


#Login
class LoginHandler(Utilities):
    def get(self):
        t = jinja_env.get_template("login.html")
        response = t.render()
        self.response.write(response)

    def post(self):
        user_sub = self.request.get("username")
        pass_sub = self.request.get("password")

        user = self.get_user_info(user_sub)

        if user:
            if hashutils.valid_pw(user_sub, pass_sub, user.pw_hash):
                self.login_user(user)
                self.redirect('/homepage')
            else:
                t = jinja_env.get_template("login.html")
                response = t.render(error="Your password is incorrect.")
                self.response.write(response)
        else:
            t = jinja_env.get_template("login.html")
            response = t.render(error="The username entered does not exist.")
            self.response.write(response)

#Logout
class LogoutHandler(Utilities):
    def get(self):
        self.logout_user()

        t = jinja_env.get_template("logout.html")
        response = t.render()
        self.response.write(response)

#TODO: Implement the about page (super easy)
"""class AboutHandler(Utilities):
"""

app = webapp2.WSGIApplication([
    ('/homepage', HomepageHandler),
    ('/resources', ResourcesHandler),
    ('/signup', SignupHandler),
    ('/s-signupq', Quiz.SignupQStartHandler),
    ('/signupq', Quiz.SignupQuizHandler), #Signup quiz handler
    ('/login', LoginHandler),
    ('/logout', LogoutHandler),
    #webapp2.Route('/<username:[a-zA-Z0-9_-]{8,20}/profile', Quiz.ProfileHandler) #TODO: Implement this

], debug=True)
