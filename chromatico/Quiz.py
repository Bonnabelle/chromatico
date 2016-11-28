from base import *
from util.quizGeneration import *

#Start page before signup quiz
class SignupQStartHandler(Utilities):
    def get(self):
        t = jinja_env.get_template("squiz-start.html")
        response = t.render()
        self.response.write(response)

#Initializes a new global set of variables to be used everywhere
counter = 1         #Counts questions answered
maxm = 1            #Variable to track custom number of questions (maximum allowed)
correct = 0         #Counts how many correct
options = None      #List of notes
answer = None       #Answer from that list ^

#Signup quiz
class SignupQuizHandler(Utilities):
    def get(self):
        global counter
        global options
        global correct
        global answer

        #If they try to retake the quiz
        if self.current_user and self.current_user.stats.taken_assess == True:
            self.redirect("/homepage")

        options = getOption(1)
        answer = getAnswer(options)
        audio = getAudio(answer)
        t = jinja_env.get_template("squiz.html")
        response = t.render(answer=answer,op1=options[0],op2=options[1],op3=options[2],op4=options[3], counter=counter,audio=audio)
        self.response.write(response)

    def post(self):
        global counter
        global answer
        global correct

        #If questions answered is less than total number of questions
        if counter < 20:
            submitted = self.request.get("option")

           #If they try to skip the question without submitting
            if submitted == "":
                counter -= 1
                self.redirect("/signupq")

            if answer == submitted:
                counter += 1
                correct += 1
                self.redirect("/signupq")
            else:
                counter += 1
                self.redirect("/signupq")
        else:
            self.current_user.stats.points += 10

            #Calculate percent
            if correct >= 1:
                percent = float(100 * correct)  / 20
            else:
                percent = 0.0

            self.current_user.stats.quizzes_complete += 1
            self.current_user.stats.percentage_correct += percent

            #Assign level
            if correct > 18:
                self.current_user.level = 3
            elif correct < 18 and correct > 11:
                self.current_user.level = 2
            else:
                self.current_user.level = 1

            self.current_user.stats.taken_assess = True

            self.current_user.stats.put() #Updates all the data in the database

            self.redirect("/results")
            #self.redirect("/%s/profile" % self.current_user.username)

class quizCustomizerHandler(Utilities):
    #TODO: Implement this class/webpage that allows a user to choose how many questions they want to do,
    # What type of questions wil be in their quiz, and then pass those on to the quizHandler to generate a quiz
    def get(self):
        t = jinja_env.get_template("qcustomize.html")
        response = t.render()
        self.response.write(response)

    def post(self):
        global maxm
        qnum = self.request.get("qnum")

        maxm = qnum
        self.redirect("/quiz")




class quizHandler(Utilities):
    def get(self):
        global options
        global correct
        global answer

        options = getOption(1)
        answer = getAnswer(options)
        audio = getAudio(answer)
        t = jinja_env.get_template("quiz.html")
        response = t.render(answer=answer,op1=options[0],op2=options[1],op3=options[2],op4=options[3], counter=counter,audio=audio)
        self.response.write(response)

    def post(self):
        global counter
        global maxm
        global answer
        global correct

        #If questions answered is less than total number of questions
        if counter <= maxm:
            submitted = self.request.get("option")

           #If they try to skip the question without submitting
            if submitted == "":
                counter -= 1
                self.redirect("/quiz")

            if answer == submitted:
                counter += 1
                correct += 1
                self.redirect("/quiz")
            else:
                counter += 1
                self.redirect("/quiz")
        else:
            self.current_user.stats.points += 10

            #Calculate percent
            if correct >= 1:
                percent = float((100 * correct)  / 20) % 100
            else:
                percent = 0.0

            self.current_user.stats.quizzes_complete += 1
            self.current_user.stats.percentage_correct += percent

            #Assign level
            if self.current_user.stats.points >= 400:
                self.current_user.level = 4
            elif self.current_user.stats.points >= 300:
                self.current_user.level = 3
            elif self.current_user.stats.points >= 200:
                self.current_user.level = 2

            self.current_user.stats.put()
            self.redirect("/results")


class ResultsHandler(Utilities):
    def get(self):
        global correct
        global counter
        t = jinja_env.get_template("results.html")
        response = t.render(current_user = self.current_user, correct=correct)
        self.response.write(response)

        #Resets all the variables for use in another quiz
        correct = 0
        counter = 1
        options = None
        answer = None
