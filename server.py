from flask import Flask, request
import config
from functions import *

def authCheck(key):
	if key in config.fsaik:
		return("ok")


app = Flask(__name__)

try:
	
	@app.route("/")
	def home():
		return("Home Page")
	
	
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
			return(f"incorrect or non-existent api key. please check your url. debug info: Service called: 'image', key: {param}")
	
	
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
			return(f"incorrect or non-existent api key. please check your url. debug info: Service called: 'chat', key: {text}")
	
	
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
			return(f"incorrect or non-existent api key. please check your url. debug info: Service called: 'name generator', key: {desc}, seed: {seed}")
	
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
			return(f"incorrect or non-existent api key. please check your url. debug info: Service called: 'horror story gen', key: {topic}")
except Exception as e:
	print(f"{e}")
	
	
if __name__ == "__main__":
	app.run(debug=True)