#to run this first run 'pipenv shell'
from turtle import title
from flask import render_template
from distutils.log import debug
from flask import Flask

app = Flask(__name__)

students = [{"regdno": 2000031242, "name": "Vinay", "course": "PFSD"},
{"regdno": 2000030558, "name": "Sai", "course": "OSD"},
{"regdno": 2000031251, "name": "Hecker Harsha Sins", "course": "AIDS"}]

@app.route("/")
def home():
    return render_template("home.html", students = students)

@app.route("/login")
def login():
    return render_template("login.html", title="Login")

@app.route("/register")
def register():
    return render_template("register.html",title="Register")

@app.route("/logout")
def logout():
    return "<h1>Your are logged out</h1>"

@app.route("/attendance")
def attendance():
    return "<p>view attendance or marks</p>"

@app.route("/profile")
def profile():
    return "<p>this is going to be your profile</p>"

@app.route("/contactus")
def contactus():
    return "<p>contact us</p>"

if __name__ == "__main__":
    app.run()
    debug = True


