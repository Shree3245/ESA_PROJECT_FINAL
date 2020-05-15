from flask import Flask, render_template, url_for, request,session, redirect,make_response, jsonify,flash, Response,send_from_directory
import re
from werkzeug.utils import secure_filename
import pathlib
from werkzeug.wsgi import FileWrapper
from random import randint
from api import *

app = Flask(__name__)

@app.route('/')
def _():
	return render_template('login.html')

@app.route("/login",methods = ['POST','GET'])
def login():
	if 'username' in session:
		return(redirect(url_for("home")))
	user = request.form['username']
	passw = request.form['password']
	print(type(authenticate(user,passw)['status']))
	if authenticate(user,passw)['status'] == 200:
		session['username']=user
		return redirect(url_for('home'))
	else:
		return(redirect(url_for("_")))

@app.route("/index")
@app.route("/index/<id>",methods = ['POST','GET'])
@app.route('/index/<method>',methods = ['POST','GET'])
def home(id=None,method=None):
	if not 'username' in session:
		return redirect(url_for("_"))
	wallet=getWallet(session['username'])['wallet']
	scooterList=(vehicle().json()['vehicleList']) 
	return render_template('index.html',balance=wallet,items=scooterList)

@app.route("/cashAdd",methods = ['POST','GET'])
def cashAdd():
	if not 'username' in session:
		return redirect(url_for("_"))
	cashAd = request.form['cashInput']
	addMoneyAccount(session['username'],cashAd).json()
	return redirect(url_for("home"))

@app.route("/driveSelect/<scooterID>")
def driveSelect(scooterID):
	pass

app.secret_key = 'mysecret'
if __name__ == "__main__":
	app.run(debug=True)
	#app.run(debug=True)

