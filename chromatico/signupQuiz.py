from base import *
from util.quizGeneration import *
#Signup Quiz

class SignupQStartHandler(Utilities):
    def get(self):
        t = jinja_env.get_template("squiz-start.html")
        response = t.render(username_error="",verify_error="")
        self.response.write(response)

    def post(self):
        username = self.request.get("username")
        username_verify = self.request.get("verify")

        if username == username_verify:
            self.redirect('/signupq')

        elif username != username_verify:
            t = jinja_env.get_template("squiz-start.html")
            response = t.render(username_error="",verify_error="Your usernames must match in order for you to continue!")
            self.response.write(response)


class SignupQuizHandler(Utilities):
    options = getOption(1)
    answer = getAnswer(options)
    def get(self):
        answer = self.answer
        options = self.options
        t = jinja_env.get_template("squiz.html")
        response = t.render(answer=answer,op1=options[0],op2=options[1],op3=options[2],op4=options[3])
        self.response.write(response)

    def post(self):
        submitted = self.request.get("option")
        if self.answer == submitted:
            self.response.out.write("YES!")
        else:
            self.response.out.write("Booooo." + submitted)



class resultsHandler(Utilities):
    def get(self):
        self.out.response.write(correct)
