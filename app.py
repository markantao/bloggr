from flask import Flask, render_template, redirect, flash, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        user = r=request.form["uname"]
        return redirect(url_for("main"))
    else:
        return render_template("signup.html")
    


@app.route("/main")
def main():
    return render_template("main.html")
    


    # return render_template("signup.html")

if __name__ == ("__main__"):
    app.run(debug="True")