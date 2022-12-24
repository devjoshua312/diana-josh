from flask import Flask, request
from functions import *
import os

def authCheck(key):
	if key in ["hlgisaiod7itygI87ghv6YUFvb8967yrfvbski328s43512c684"]:
		return("ok")

app = Flask(__name__)
apiError = "incorrect or non-existent api key. please check your url."

@app.route("/")
def home():
	return("Created by Esvin Joshua.")



@app.route("/image")
def image_gen():
	param = request.args.get("param")
	kkey = request.args.get("api_key")
	if authCheck(kkey) == "ok":
		try:
			img = image(param)
			return(img)
		except Exception as e:
			return(f"{e}")
	else:
		return(apiError)


@app.route("/chat")
def chat_bot():
	kkey = request.args.get("api_key")
	text = request.args.get("text")
	if authCheck(kkey) == "ok":
		try:
			msg = friend(text)
			return(msg)
		except Exception as e:
			return(f"{e}")
	else:
		return(apiError)

@app.route("/aichat")
def aichat():
	msg = request.args.get("msg")
	kkey = request.args.get("api_key")
	if authCheck(kkey) == "ok":
		try:
			con = convo(msg)
			return(con)
		except Exception as e:
			return(f"{e}")
	else:
		return(apiError)


@app.route("/name")
def name_gen():
	kkey = request.args.get("api_key")
	desc = request.args.get("des")
	seed = request.args.get("seed")
	if authCheck(kkey) == "ok":
		try:
			prd = name(desc, seed)
			return(prd)
		except Exception as e:
			return(f"{e}")
	else:
		return(apiError)

@app.route("/horror")
def scare():
	topic = request.args.get("top")
	kkey = request.args.get("api_key")
	if authCheck(kkey) == "ok":
		try:
			story = horror(topic)
			return(story)
		except Exception as e:
			return(f"{e}")
	else:
		return(apiError)

@app.route("/recipe")
def recipee():
	ingre = request.args.get("ingredients")
	kkey = request.args.get("api_key")
	if authCheck(kkey) == "ok":
		try:
			recipe(ingre)
			return(recipe)
		except Exception as e:
			return(f"{e}")
	else:
		return(apiError)


if __name__ == "__main__":
	app.run(debug=True)