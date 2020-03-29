from mongoengine import *
from bson.json_util import dumps
from random import randint
from datetime import datetime
connect('Vehicle')


class ExistCar(Document):
	car = StringField(required=True)
	device = StringField(required=True)

class User(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    Name = StringField(required=True)
    bank = StringField()
    wallet = FloatField()

class PaymentHistory(Document):
    userID = StringField(required=True)
    fromUser = StringField(required=True)
    timeStamp = DateTimeField(required=True)
    payment = FloatField(required=True)

class CustomerHistory(Document):
    userID = StringField(required=True)
    timeStamp = DateTimeField(required=True)
    duration=FloatField
    (required=True)
    cost = FloatField(required=True)

def userInsert(username,pasword,name):
	user=User(
		
		username = username,
		password = pasword,
		Name = name,
        bank ="Bank of ESA",
        wallet = randint(1,3000)
	 
	)
	user.save() 

def createTransaction(username,duration,cost):
	transaction=CustomerHistory(
		
		userID = username,
		timeStamp = datetime.now(),
		duration = duration,
        cost = cost
	 
	)
	transaction.save() 