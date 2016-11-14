from base import *
from util.quizGeneration import *
#Signup Quiz
current_user_username = ""
current_q = None #This should hold the current quiz.
correct = 0

class SignupQStartHandler(Utilities):
    def get(self):
        t = jinja_env.get_template("squiz-start.html")
        response = t.render(username_error="",verify_error="")
        self.response.write(response)

    def post(self):
        username = self.request.get("username")
        username_verify = self.request.get("verify")

        if username == username_verify:
            current_user_username = username
            current_quiz = Quiz(total_q=20,q_complete=0,q_correct=0,points_given=10)
            current_quiz.put()
            current_q = current_quiz #TODO: This isn't working, it won't update the variable.
            self.redirect('/signupq')
        elif username != username_verify:
            t = jinja_env.get_template("squiz-start.html")
            response = t.render(username_error="",verify_error="Your usernames must match in order for you to continue!")
            self.response.write(response)



class SignupQuizHandler(Utilities):
    def get(self):
        options = getOption(1)
        answer = getAnswer(options)

        t = jinja_env.get_template("squiz.html")
        response = t.render(answer=answer,options=options)
        self.response.write(response)

    def post(self):
        self.repsponse.out.write(correct)
        if correct < 20:
            submitted = self.request.get("option")
            answer = self.request.get("answer")

            if submitted == answer:
                correct += 1
            else:
                self.redirect("/signupq")
        else:
            correct = 0
            self.response.out.write("You got", correct, " out of 20 correct. Good job!" )

"""
class SignupQuizHandler(Utilities):
    def get(self):
        self.response.out.write(current_q)

    options = getOption(1) #Gets 4 random notes
    answer = getAnswer(options) #Chooses answer out of above variable
    #current_user = self.get_user_info(current_user_username)
    #user_stats = self.get_user_stats(current_user)

    def get(self):
        current_user = self.get_user_info(current_user_username)
        user_stats = self.get_user_stats(current_user)

        if self.current_quiz.q_complete == self.current_quiz.total_q:
            current_user.taken_assess = True
            current_user.level += new_level
            user_stats.quizzes_complete += 1
            user_stats.percentage_correct += percent

            self.redirect("/results")
        else:
            t = jinja_env.get_template("squiz.html")
            response = t.render(options=self.options,answer=self.answer) #The answer is being shown for testing
            self.response.write(response)

    def post(self):
        #user_stats = self.get_user_stats(self.user)
        answer = self.answer

        self.current_quiz.q_complete += 1

        submitted = self.request.get("option")
        if submitted == answer:
            self.current_quiz.q_correct += 1
            #user_stats.percentage_correct += 1.0
        #else:
            #user_stats.percentage_correct -= 1.0

        self.redirect("/signupq")
"""

class resultsHandler(Utilities):
    def get(self):
        self.out.response.write("WoooOooOoOooo")
