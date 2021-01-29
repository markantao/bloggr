from flask import Flask, render_template, redirect, flash, url_for, request, session, datetime
from datetime import timedelta
from flask_sqlalchemy import SQLAlcehmy

app = Flask(__name__)
app.secret_key = "blogrr_project"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.permanent_session_lifetime = timedelta(weeks=52)

db = SQLAlcehmy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), unique=True, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', {self.email})'"

Class Post(db.Model):
    id = db.Column(db.Intefer, primary_key=True)
    tite = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text(500), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}', '{self.content})"



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