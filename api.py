from requests import put, get,post  
import json

def authenticate(username,password,url="http://127.0.0.1:5000"):
	temp = get("{}/User_authenticate".format(url),data={
			'User':username,
			'Password':password
			} )
	return temp

def addUser(username,password,name,url="http://127.0.0.1:5000"):
	temp = put("{}/User_authenticate".format(url),data={
			'User':username,
			'Password':password,
			"Name":name
			} )
	return temp

def addMoneyAccount(username,payment,url="http://127.0.0.1:5000"):
	temp = put("{}/Banking_transaction".format(url),data={
			'User':username,
			"payment":payment
			} )
	return temp

def getWallet(username,url ="http://127.0.0.1:5000" ):
	temp = get("{}/Banking_transaction".format(url),data={
			'User':username
			} )
	return temp	

def makeTransaction(username,payment,duration,url="http://127.0.0.1:5000"):
	temp = put("{}/Payment_transaction".format(url),data={
			'User':username,
			"payment":payment,
			'duration':duration
			} )
	return temp

def customerHistory(username,url="http://127.0.0.1:5000"):
	temp = get("{}/Payment_transaction".format(url),data={
			'User':username
			} )
	return temp

def totalTransactionHistory(url="http://127.0.0.1:5000"):
	temp = get("{}/Payment_transaction".format(url))
	return temp
# url = "http://127.0.0.1:5000"
# #x = addUser("user1","pass1",'Name',url)
# x = authenticate("user1",'pass1',url)
# #x = getWallet('user1')
# #x= totalTransactionHistory()
# print(x.status_code)
# print(x.json())
# x=json.loads(x.json())
# print(x)
   