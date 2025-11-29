#it will be filled with the flask app code
from flask import Flask

@app.route("/")
def home():
	return "Hello Worls from Kubernetes!"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
