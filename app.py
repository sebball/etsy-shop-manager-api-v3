from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
import os
import authorization

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == "GET":
        if request.args["code"]:
            # response from authorization request containing code. Use code as arg to the func request_token to perform
            # a PUT request (request_token func) and receive the response dictionary containing access and refresh token
            code = request.args["code"]
            response_dict = authorization.request_token(code_string=code)
            print(token_dict)
            return redirect("/welcome")

        else:
            return "<p>Hello, World! <a href=/auth-redirect> Authorize here </a></p>"





@app.route("/auth-redirect")
def authorize():
    return redirect(authorization.authorize_account())

@app.route("/welcome")
def manager_home():
    return "hi what you wanna do?"