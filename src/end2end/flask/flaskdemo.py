from flask import Flask, render_template, request
from sense_hat import SenseHat
import pyrebase
import time

app = Flask(__name__)
sense = SenseHat()

config = {
    "apiKey": "AlzaSyBugZNEeK_HK1534mP9RUw0HS0c-KfhLqw",
    "authDomain": "mocktenderdb.firebaseapp.com",
    "databaseURL": "https://mocktenderdb-default-rtdb.firebaseio.com/",
    "storageBucket": "mocktenderdb.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

flasktitle = "L3-G8 end-to-end demo"

@app.route("/")
def index():
    db.child("button").remove()
    return render_template('index.html')

@app.route("/button-test")
def function():
    sense.clear((0,255,0))
    time.sleep(0.1)
    sense.clear()
    dtime = time.strftime("%Y-%m-%d %H:%M:%S")
    db.child("button").child(dtime).set("pressed")
    return render_template('buttonpressed.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
