#it will be filled with the flask app code
from flask import Flask
import os
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World from Kubernetes!!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "test")
DB_USER = "root"
DB_PASS = os.getenv("DB_ROOT_PASSWORD", "root")

conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASS,
    database=DB_NAME
)
