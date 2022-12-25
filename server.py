from flask import Flask, request
from functions import *

def authCheck(key):
	if key in ["hlgisaiod7itygI87ghv6Yiusgrfvbski328s43512c684"]:
		return("ok")


app = Flask(__name__)
apiError = "incorrect or non-existent api key. please check your url."

@app.route("/")
def home():
	return("Created by Esvin Joshua.")



@app.route("/image")
def image_gen():
	text = request.args.get("text")
	kkey = request.args.get("api_key")
	if authCheck(kkey) == "ok":
		try:
			img = image(text)
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
	text = request.args.get("text")
	kkey = request.args.get("api_key")
	if authCheck(kkey) == "ok":
		try:
			con = convo(text)
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
	text = request.args.get("text")
	kkey = request.args.get("api_key")
	if authCheck(kkey) == "ok":
		try:
			story = horror(text)
			return(story)
		except Exception as e:
			return(f"{e}")
	else:
		return(apiError)

@app.route("/recipe")
def recipee():
	text = request.args.get("text")
	kkey = request.args.get("api_key")
	if authCheck(kkey) == "ok":
		try:
			r = recipe(text)
			return(r)
		except Exception as e:
			return(f"{e}")
	else:
		return(apiError)


if __name__ == "__main__":
	app.run(debug=True)