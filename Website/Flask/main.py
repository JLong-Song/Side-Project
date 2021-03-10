from flask import Flask, render_template, request
from mysql.connector import *
app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=['POST'])
def login():
    account = request.values.get('Account')
    password = request.values.get('Password')


def sql_connection():
    #connection = mysql.connector.connect(host='localhost')


if __name__ == '__main__':
    app.run()
