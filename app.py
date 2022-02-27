from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
app=Flask(__name__)

@app.route('/signup',methods=['GET','POST'])
def signup():
  if request=="POST": 
        
  return render_template('signup.html')

if __name__=='__main__':
  app.run()
