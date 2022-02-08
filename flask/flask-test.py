# Eric Liu
# Topics flask 
# Copied file form repl.it
# Not working 100%, need to continue work on it.

from flask import Flask
from app import app

app = Flask('app')

@app.route('/')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

