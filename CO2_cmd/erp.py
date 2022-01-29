from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route("/login")
def login():
    return "<p>login to kl erp</p>"

@app.route("/register")
def register():
    return "<p>register to kl erp</p>"

@app.route("/logout")
def logout():
    return "<p>logout page</p>"

@app.route("/attendance")
def attendance():
    return "<p>view attendance or marks</p>"

@app.route("/")
def home():
    return "<p>welcome to kl erp</p>"

@app.route("/profile")
def profile():
    return "<p>this is going to be your profile</p>"

@app.route("/contactus")
def contactus():
    return "<p>contact us</p>"

if __name__ == "__main__":
    app.run()
    debug = True


