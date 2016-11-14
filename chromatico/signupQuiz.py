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

    """def post
    options = getOption(1) #Gets 4 random notes
    answer = getAnswer(options) #Chooses answer out of above variable
"""
    #TODO: Implement way to randomly generate 20 questions and then take the user to their profile, with all their new statistics
