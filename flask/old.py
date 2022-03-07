# Eric Liu
# Topics flask 

from flask import Flask
from app import app
from flask import render_template

import random

app = Flask('app')

@app.route("/rand")
def randomnumber():
  i = random.randrange(100)
  return render_template("lucky.html",number = i)

@app.route("/")
def index():
  return "<h1>Hello World from my computer !</h1>"


app.run(host="0.0.0.0",port=5000,debug=True)
