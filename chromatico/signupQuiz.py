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
        t = jinja_env.get_template("squiz.html")
        response = t.render(options=options,answer=answer) #The answer is being shown for testing
        self.response.write(response)

    def post(self):
        options = getOption(1) #Gets 4 random notes
        answer = getAnswer(options) #Chooses answer out of above variable
        counter = 0 #Counter to count how many questions they've completed

        username = webapp2.request.get("username")
        current_user = Utilites.get_user_info(username) #Gets user info
        user_stats = Utilites.get_user_stats(current_user)
        
        selected = self.request.get("option") #Gets user selection
        while counter <= 20:
            if selected == answer:
                counter += 1
                user_stats.percentae_correct += 1.0
                self.redirect("/signupq")
            else:
                counter += 1
                user_Stats.percentae_correct -= 1.0
                self.redirect("/signupq")
        current_user.taken_assess = True

        if user_stats.percentage_correct > 18.0:
            current_user.level = 3
        elif user_stats.percentage_correct < 18.0 and user_stats.percentage_correct > 6.0:
            current_user.level = 2
        else:
            curent_user.level = 1

        self.redirect("/homepage")
