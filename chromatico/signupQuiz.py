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

#Initializes a new set of options and their answer, a counter to count questions completed and a variable to track correct answers. to be used throughout the quizzes
counter = 0
correct = 0
options = None
answer = None

class SignupQuizHandler(Utilities):
    def get(self):
        global counter
        global options
        global correct
        global answer
        options = getOption(1)
        answer = getAnswer(options)
        t = jinja_env.get_template("squiz.html")
        response = t.render(answer=answer,op1=options[0],op2=options[1],op3=options[2],op4=options[3], counter=counter,correct=correct)
        self.response.write(response)

    def post(self):
        global counter
        global answer
        global correct

        if counter <= 19:
            submitted = self.request.get("option")
            #self.response.out.write("User submitted: " + submitted + ", and the answer it was compared to was: " + answer)
            if answer == submitted: #TODO: Fix this- it's not comparing them correctly
                counter += 1
                correct += 1
                self.redirect("/signupq")
            #TODO: Get user from database taking the quiz
            #TODO: Add these stats after they are at 20 questions
            else:
                counter += 1
                self.redirect("/signupq")
        else:
            self.redirect("/results")
            


#For debugging
class resultsHandler(Utilities):
    def get(self):
        self.response.out.write("You got " + str(correct) + " out of 20 questions correct. Congratulations!") #TODO: This will redirect the user to their profile page with the results
