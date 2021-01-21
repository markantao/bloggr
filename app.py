from flask import Flask, render_template, redirect, flash, url_for, request, session

app = Flask(__name__)
app.secret_key = "blogrr_project"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        user = r=request.form["uname"]
        session["user"] = user
        return redirect(url_for("main"))
    else:
        return render_template("signup.html")
    


@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("signup"))
    


    # return render_template("signup.html")

if __name__ == ("__main__"):
    app.run(debug="True")