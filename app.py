from flask import Flask
from flask import redirect
from flask import render_template

app=Flask(__name__)

@app.route('/signup')
def signup():
  return render_template('signup.html')
