from base import *
from util.quizGeneration import *

#Start page before signup quiz
class SignupQStartHandler(Utilities):
    def get(self):
        t = jinja_env.get_template("squiz-start.html")
        response = t.render()
        self.response.write(response)

#Initializes a new global set of variables to be used everywhere
counter = 0         #Counts questions
maxm = 1            #Variable to track custom number of questions (maximum allowed)
correct = 0         #Counts how many correct
options = None      #List of notes
answer = None       #Answer from that list ^
typ = None

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

        options = getTextOption(1)
        answer = getAnswer(options, 0)
        audio = getAudio(answer)
        t = jinja_env.get_template("squiz.html")
        response = t.render(op1=options[0],op2=options[1],op3=options[2],op4=options[3], counter=counter,audio=audio)
        self.response.write(response)

    def post(self):
        global counter
        global answer
        global correct

        #If questions answered is less than total number of questions
        if counter <= 19:
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
            self.current_user.stats.percentages.append(percent)

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

class QuizCustomizerHandler(Utilities):
    #TODO: Implement this class/webpage that allows a user to choose how many questions they want to do,
    # What type of questions wil be in their quiz, and then pass those on to the quizHandler to generate a quiz
    def get(self):
        t = jinja_env.get_template("qcustomize.html")
        response = t.render()
        self.response.write(response)

    def post(self):
        global typ
        global maxm
        qnum = self.request.get("qnum")
        qnum = int(qnum)

        qtype = self.request.get("type")
        typ = qtype

        maxm = qnum
        self.redirect("/quiz")

class QuizHandler(Utilities):
    def get(self):
        global options
        global correct
        global answer
        global maxm
        global typ

        audio = ""

        if typ == "Text":
            options = getTextOption(self.current_user.level)
            answer = getAnswer(options,"Text")
            audio = getAudio(answer)
        elif typ == "Audio":
            options = getAudioOption(self.current_user.level)
            answer = getAnswer(options,"Audio")
        elif typ == "Random":
            boo = random.randrange(0,2)
            options = getRandomOption(self.current_user.level, boo)
            answer = getAnswer(options, boo)
            if boo == 0:
                audio = answer

        t = jinja_env.get_template("quiz.html")
        response = t.render(options=options, counter=counter,note=answer,audio=audio)
        self.response.write(response)

    def post(self):
        global counter
        global maxm
        global answer
        global correct

        #If questions answered is less than total number of questions
        if counter < maxm:
            submitted = self.request.get("option")

           #If they try to skip the question without submitting
            if submitted == "":
                counter -= 1
                self.redirect("/quiz")

            if answer == submitted or submitted == all_freq.get(answer):
                counter += 1
                correct += 1
                self.redirect("/quiz")
            else:
                counter += 1
                self.redirect("/quiz")
        else:
            self.current_user.stats.points += correct

            #Calculate percent
            if correct >= 1:
                percent = float(((100 * correct)  / 20) * 10) % 101
            else:
                percent = 0.0

            self.current_user.stats.quizzes_complete += 1
            self.current_user.stats.percentages.append(percent)

            #Assign level
            if self.current_user.stats.points >= 400:
                self.current_user.level = 4
            elif self.current_user.stats.points >= 300:
                self.current_user.level = 3
            elif self.current_user.stats.points >= 200:
                self.current_user.level = 2

            self.current_user.stats.put()
            self.redirect("/results")
            #TODO: Make this work.
            #self.redirect("/%s/profile" % self.current_user.username)


class ResultsHandler(Utilities):
    def get(self):
        global correct
        global counter
        global maxm
        percent = float((100 * correct)  / counter) % 101
        t = jinja_env.get_template("results.html")
        response = t.render(current_user = self.current_user, correct=correct,counter=counter,percent=percent)
        self.response.write(response)

        #Resets all the variables for use in another quiz
        correct = 0
        counter = 0
        maxm = 1
        options = None
        answer = None
