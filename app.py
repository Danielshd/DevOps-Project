<<<<<<< HEAD
from flask import Flask, jsonify
import mysql.connector
import os
=======
#it will be filled with the flask app code
from flask import Flask
import os
import mysql.connector
>>>>>>> 4c36fb9740b783d66194b50e1d41a8086f97fb66

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.route("/")
def home():
    return "Flask + MySQL running on EKS!"

@app.route("/users")
def users():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM users;")
    result = cursor.fetchall()
    return jsonify(result)

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
