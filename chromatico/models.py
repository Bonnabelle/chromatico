from google.appengine.ext import db

class User(db.Model):
    username = db.StringProperty(required = True)
    pw_hash = db.StringProperty(required = True) #Hash generated from password
    email = db.StringProperty()
    taken_assess = db.BooleanProperty(required = True)
    level = db.IntegerProperty() #Assigned from quiz

class UserStats(db.Model):
    statistics_owner = db.StringProperty(required=True)
    quizzes_complete = db.IntegerProperty()
    percentage_correct = db.FloatProperty()
    points = db.IntegerProperty()

#TODO: Make another model for a user-created quiz
