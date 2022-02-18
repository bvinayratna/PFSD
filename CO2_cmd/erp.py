#to run this first run 'pipenv shell'
from turtle import title
from flask import render_template
from distutils.log import debug
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

semesters = ["Select Semester","Odd Sem", "Even Sem", "Summer Term"]

years =[{"year": "Select Academic year"},{"year":"2021-2022"},
{"year":"2020-2021"},
{"year":"2019-2020"}]

students = [{"regdno": 2000031242, "name": "Vinay", "course": "PFSD"},
{"regdno": 2000030558, "name": "Sai", "course": "OSD"},
{"regdno": 2000031251, "name": "Hecker", "course": "Hacking"}]

flag=1

@app.route("/")
def home():
    return render_template("home.html", students = students,title="Home")

@app.route("/courses")
def courses():
    return render_template("course_pages/courses.html",title="Courses", years=years,semesters=semesters, flag=flag)

@app.route("/login")
def login():
    return render_template("login.html", title="Login")

@app.route("/handouts")
def handouts():
    return render_template("course_pages/handouts.html", years=years,semesters=semesters,title="Handouts",flag=flag)

@app.route("/materials")
def materials():
    return render_template("course_pages/materials.html", years=years,semesters=semesters,title="Materials",)

@app.route("/assignments")
def assignments():
    return render_template("course_pages/assignments.html", years=years,semesters=semesters,title="Assignments",)

@app.route("/internals")
def internals():
    return render_template("course_pages/internals.html", years=years,semesters=semesters,title="Internals",)

@app.route("/register")
def register():
    return render_template("register.html",title="Register")

@app.route("/logout")
def logout():
    return "<p>Your are logged out! <br>Thank you</p>"

@app.route("/attendance")
def attendance():
    return render_template("attendance.html", title="Attendance")

@app.route("/profile")
def profile():
    return render_template("profile.html", title="Profile")

@app.route("/contactus")
def contactus():
    return render_template("contactus.html", title="Contact-us")

if __name__ == "__main__":
    app.run()
    debug = True


