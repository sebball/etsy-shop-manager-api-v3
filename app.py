from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
import os

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == "GET":
        return "<p>Hello, World! <a href=/auth-redirect> Authorize here <a>p>"
    elif request.method == "POST":
        data = request.form
        print(data)


# @app.route("/auth-redirect")
# def authorize():
#     return "<p> "