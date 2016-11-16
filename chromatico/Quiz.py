from base import *
from util.quizGeneration import *

#Start page before signup quiz
class SignupQStartHandler(Utilities):
    def get(self):
        t = jinja_env.get_template("squiz-start.html")
        response = t.render(username_error="")
        self.response.write(response)

    def post(self):
        global current_user
        global current_user_stats

        username = self.request.get("username")
        user = self.get_user_info(username)
        if username == "" or user == None:
            t = jinja_env.get_template("squiz-start.html")
            response = t.render(username_error="Make sure your username is spelled correctly.")
            self.response.write(response)
        else:
            current_user = user
            current_user_stats = self.get_user_stats(current_user.username)
            self.redirect('/signupq')

#Initializes a new global set of options and their answer, a counter to count questions completed and a variable to track correct answers.
counter = 0
correct = 0
options = None
answer = None

#Signup quiz
class SignupQuizHandler(Utilities):
    def get(self):
        global counter
        global options
        global correct
        global answer

        #If they try to access the quiz without permission
        if self.request.path == "/signupq" and current_user == None:
            self.redirect("/s-signupq")

        #If they try to retake the quiz
        elif current_user.taken_assess == True:
            self.redirect("/homepage")

        options = getOption(1)
        answer = getAnswer(options)
        t = jinja_env.get_template("squiz.html")
        response = t.render(answer=answer,op1=options[0],op2=options[1],op3=options[2],op4=options[3], counter=counter,correct=correct,audio="")
        self.response.write(response)

    def post(self):
        global current_user
        global current_user_stats
        global counter
        global answer
        global correct

        if counter < 20:
            submitted = self.request.get("option")
            if answer == submitted:
                counter += 1
                correct += 1
                self.redirect("/signupq")
            else:
                counter += 1
                self.redirect("/signupq")
        else:
            current_user.taken_assess = True

            current_user_stats.points += 10

            #Calculate percent
            if correct > 1:
                percent = float(20/correct)
            else:
                percent = 1.0
            current_user_stats.quizzes_complete += 1
            current_user_stats.percentage_correct += percent

            #Assign level
            if correct > 18:
                current_user.level = 3
            elif correct < 18 and correct > 11:
                current_user.level = 2
            else:
                current_user.level = 1

            self.redirect("/%s/profile" % current_user.username)



"""class ProfileHandler(Utilities):
    def get(self,username = current_user.username):
        global correct
        global current_user
        global current_user_stats

        self.response.out.write("You got " + str(correct) + " out of 20 questions correct. Congratulations! Your level is now: " + str(current_user.level) +
        " and your total percentage correct is: " + str(current_user_stats.percentage_correct) + ". You're ready to begin training!")
"""
