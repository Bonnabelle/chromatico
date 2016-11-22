from google.appengine.ext import db

class UserStats(db.Model):
    taken_assess = db.BooleanProperty(required = True)
    quizzes_complete = db.IntegerProperty()
    percentage_correct = db.FloatProperty()
    points = db.IntegerProperty()

class User(db.Model):
    username = db.StringProperty(required = True)
    pw_hash = db.StringProperty(required = True) #Hash generated from password
    email = db.StringProperty()
    level = db.IntegerProperty() #Assigned from quiz
    stats = db.ReferenceProperty(UserStats)
