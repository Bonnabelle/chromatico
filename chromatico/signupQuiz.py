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

counter = 0
correct = 0

class SignupQuizHandler(Utilities):
    def get(self):
        #TODO: Make it possible for either this set of two methods to recreate themselves every time a user is redirected
        #Or make it possible to access the answer from post
        options = getOption(1)
        answer = getAnswer(options)
        global counter
        t = jinja_env.get_template("squiz.html")
        response = t.render(answer=answer,op1=options[0],op2=options[1],op3=options[2],op4=options[3], counter=counter)
        self.response.write(response)

    def post(self):
        global counter
        global correct

        if counter <= 19:
            submitted = self.request.get("option")
            if self.answer == submitted:
                counter += 1
                correct += 1
                self.redirect("/signupq")
            #TODO: Get user from database taking the quiz
            #TODO: Add these stats after they are at 20 questions
            else:
                counter += 1
                self.redirect("/signupq")
        self.response.out.write("You got " + str(correct) + " out of 20 questions correct. Congratulations!") #TODO: This will redirect the user to their profile page with the results



class resultsHandler(Utilities):
    def get(self):
        self.out.response.write(correct)
