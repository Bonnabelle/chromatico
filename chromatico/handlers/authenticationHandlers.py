from base import *

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

        user = validations.validate_username(sub_user)
        pas = validations.validate_password(sub_pass)
        pas_ver = validations.validate_verify(sub_pass,sub_pass_ver)
        em = validations.validate_email(sub_em)

        if user != False and pas != False and pas_ver != False and sub_em != False:
            pw_hash = hashutils.make_pw_hash(user, pas)
            user = User(uid = 10, username=user, pw_hash=pw_hash, taken_assess = False, email = em) #TODO: Implement unique uid
            user.put()
            self.login_user(user)
            
            self.redirect('/quiz')
        else:
            error = True

            if user == False:
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


class LogoutHandler(Utilities):
    def get(self):
        self.logout_user()

        t = jinja_env.get_template("logout.html")
        response = t.render()
        self.response.write(response)
