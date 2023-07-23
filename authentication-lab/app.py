from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


config = {
  "apiKey": "AIzaSyBhFQpx21s3QbZqYBdcCFRikoc7kW2l8uc",
  "authDomain": "first-log-69e7d.firebaseapp.com",
  "projectId": "first-log-69e7d",
  "storageBucket": "first-log-69e7d.appspot.com",
  "messagingSenderId": "963677552448",
  "appId": "1:963677552448:web:f7bb478a9860dbafeb84a5",
  "measurementId": "G-83FEYBYXC8",
  "databaseURL": ""
}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
   error = ""
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
       except:
           error = "Authentication failed"
   return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():

    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)