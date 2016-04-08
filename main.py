#!/bin/env python

from flask import Flask, render_template

app = Flask(__name__)


# routes
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_otp')
def get_otp():
    return render_template("get_otp.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/account')
def account():
    return render_template("account.html")

if __name__ == "__main__":
    app.run()
