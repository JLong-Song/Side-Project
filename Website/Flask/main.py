from flask import Flask, render_template, request
from security import crc_16, login_confirm
app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    account = request.values.get("Account")
    password = request.values.get("Password")
    success = login_confirm(account, password)
    if success:
        return render_template("login.html", status="success")
    else:
        return render_template("login.html", status=success)


@app.route("/user", methods=["POST"])
def user():
    status = request.values.get("status")
    return render_template("user.html", status=status)


if __name__ == "__main__":
    app.run()
