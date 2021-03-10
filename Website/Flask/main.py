from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=['POST'])
def login():
    account = request.values.get('Account')
    password = request.values.get('Password')


if __name__ == '__main__':
    app.run()
