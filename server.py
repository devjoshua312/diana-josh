from flask import Flask, request
from functions import *

def authCheck(key):
	if key in ["hlgisaiod7itygI87ghv6YUFvb8967yrfvbski"]:
		return("ok")


app = Flask(__name__)

@app.route("/")
def home():
	return("Home Page")


@app.route("/image")
def image_gen():
	kkey = request.args.get("api_key")
	if authCheck(kkey) == "ok":
		param = request.args.get("param")
		img = image(param)
		return(img)
	else:
		return("Bad request.")

@app.route("/chat")
def chat_bot():
	kkey = request.args.get("api_key")
	if authCheck(kkey) == "ok":
		text = request.args.get("text")
		msg = friend(text)
		return(msg)
	else:
		return("Bad request. Service contacted: chat")


if __name__ == "__main__":
	app.run(debug=True)