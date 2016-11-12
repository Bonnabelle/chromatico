from google.appengine.ext import db

class User(db.Model):
    uid = db.IntegerProperty(required = True) #Unique hashed user id
    username = db.StringProperty(required = True)
    pw_hash = db.StringProperty(required = True) #Hash generated from password
    email = db.StringProperty()
    taken_assess = db.BooleanProperty(required = True)
    level = db.IntegerProperty() #Assigned from quiz

class UserStats(db.Model):
    user = db.ReferenceProperty(User)
    quizzes_complete = db.IntegerProperty()
    percentage_correct = db.FloatProperty()

#TODO: Make another model for a user quiz
