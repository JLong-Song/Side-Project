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
    if login_confirm(account, password):
        return "<p>Success!</p>"
    else:
        return f"<p>{account}</p><p>{crc_16(password)}</p>"


if __name__ == "__main__":
    app.run()
