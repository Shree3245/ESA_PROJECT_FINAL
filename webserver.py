from flask import Flask, request
from flask_restful import Resource, Api
from mongoengine import Q
from db import User, userInsert, createTransaction,CustomerHistory
app = Flask(__name__)
api = Api(app)


class UserAuth(Resource):
	def get(self):
		print("hello")
		user=(request.form['User'])
		password=(request.form['Password'])
		print(user)
		if not User.objects(Q(username=user) & Q(password=password)):
			return {"error": 'User not found'}
		else:
			return 200

	def put(self):
		
		user=(request.form['User'])
		password=(request.form['Password'])
		name = request.form['Name']
		userInsert(user,password,name)


class BankingAuth(Resource):
	def get(self):
		username=(request.form['User'])
		if not User.objects(username=username):
			return {"error": 'User not found'}, 404
		else:
			return User.objects().to_json(),200

	def put(self):
		
		user=(request.form['User'])
		print(user)
		if not User.objects(username=user):
			return {"error": 'User not found'}, 404
		else:
			payment = request.form['payment']
			temp = User.objects.get(username=user)
			temp.wallet = temp.wallet + float(payment)
			temp.save()    
			return User.objects().to_json(),200

class TransactionApp(Resource):
	def get(self):
		try:
			user=(request.form['User'])
		except:
			user = None
		if user != None:
			print(user)
			if not User.objects(username=user):
				return {"error": 'User not found'}, 404
			else:
				return CustomerHistory.objects(userID = user).to_json(),200
		else:
			print()
			return CustomerHistory.objects().to_json(),200


	def put(self):
		
		user=(request.form['User'])
		print(user)
		if not User.objects(username=user):
			return {"error": 'User not found'}, 404
		else:
			payment = request.form['payment']
			temp = User.objects.get(username=user)
			temp.wallet = temp.wallet -float(payment)
			temp.save() 
			duration = request.form['duration']
			createTransaction(user,duration,payment)
			return User.objects().to_json(),200

api.add_resource(UserAuth, '/User_authenticate')
api.add_resource(BankingAuth, '/Banking_transaction')
api.add_resource(TransactionApp, '/Payment_transaction')


if __name__ == '__main__':
	app.run(debug=True)




### Check if connected to internet
# import socket


# def is_connected():
#     try:
#         # connect to the host -- tells us if the host is actually
#         # reachable
#         socket.create_connection(("www.google.com", 80))
#         return True
#     except OSError:
#         pass
#     return False