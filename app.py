from flask import Flask, render_template, redirect, flash, url_for, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "blogrr_project"

app.permanent_session_lifetime = timedelta(weeks=52)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        user = request.form["uname"]
        session["user"] = user
        return redirect(url_for("main"))
    else:
        return render_template("signup.html")
    
@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for("home"))

@app.route("/main")
def main():
    if "user" in session:
        return render_template("main.html")
    else:
        return render_template("home.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("signup"))
    
@app.route("/blog")
def blog():
    if "user" in session:
        return render_template("blogging.html")


    # return render_template("signup.html")

if __name__ == ("__main__"):
    app.run(debug="True")