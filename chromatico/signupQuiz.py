from base import *
from util.quizGeneration import *
#Signup Quiz

class SignupQStartHandler(Utilities):
    def get(self):
        """if current_user.taken_assess == True or current_user == False: #If they've taken the assesment already or aren't a user
            self.redirect("/homepage")""" #Will put this back once the quiz generation starts to work
        #else:
        t = jinja_env.get_template("squiz-start.html")
        response = t.render()
        self.response.write(response)

class SignupQuizHandler(Utilities):
    def get(self):
        counter_cookie = self.request.cookies.get('visits')

        counter = int(counter_cookie)
        #TODO: Make these cookies actually count

        if counter > 20:
            self.redirect("/homepage") #TODO: This will redirect the user to their new profile with their statistics

        options = getOption(1) #Gets 4 random notes
        answer = getAnswer(options) #Chooses answer out of above variable

        counter += 1

        t = jinja_env.get_template("squiz.html")
        response = t.render(options=options,answer=answer,counter=counter) #The answer is being shown for testing
        self.response.write(response)

    def post(self):
        #submitted = self.request.get("option")
        #if submitted == answer:
        #    user_stats.percentage_correct += 1.0
        self.redirect("/signupq")
    #TODO: Count how many times the user got the answer right
