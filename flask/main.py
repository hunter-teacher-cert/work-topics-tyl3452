from flask import Flask, request,session 
from flask import render_template

import random

app = Flask(__name__)
app.secret_key="something"

# Example of a route that passes
# data to a template
@app.route("/rand")
def randomnumber():
  i = random.randrange(100)
  return render_template("lucky.html",number = i )

# the "root" route
@app.route("/")
def index():
  #return "<h1>Hello Main Page from Repl.it!</h1>"
    return render_template("index.html")

# to to an about Me website about me!
@app.route("/me")
def me():
  return render_template("me.html")

# class website
@app.route("/apcsp")
def apcsp():
  return render_template("apcsp.html")

# example of static content
# like an image or including css
@app.route("/indie")
def indie():
  return render_template("indie.html")


    
@app.route("/form_demo",methods=['GET','POST'])
def form_demo():
  # GET is when we just load the page in our browser
  # POST is when we click the button 
  if request.method=="GET":
    return render_template("form_demo.html")
  else:
    # here we clicked the button
    # so we can check the form data
    name = request.form['username']
    pw = request.form['password']
    print(name,pw)
    if pw != "12345":
      error = "BAD PASSWORD"
      name=""
    else: 
      error = ""
      
    return render_template("form_demo.html",error=error, name=name)
      
@app.route("/comments",methods=['GET','POST'])
def comments():
  # GET is when we just load the page in our browser
  # POST is when we click the button 
  if request.method=="GET":
    return render_template("comments.html")
  else:
    # here we clicked the button
    # so we can check the form data
    fname = request.form['First Name']
    lname = request.form['Last Name']
    period = request.form['period']
    comments = request.form['comments']
    print(fname,lname,period,comments)
    return render_template("comments.html", fname=fname)

      

@app.route("/session_demo")
def session_demo():

  print(session)
  if 'count' not in session:
    session['count'] = 1
  else:
    session['count'] = session['count'] + 1

  return render_template('session_demo.html',count = session['count'])
 
  
app.run(host="0.0.0.0",port=5000,debug=True)