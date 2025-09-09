import flask
from flask import request, jsonify, render_template

app = flask.Flask(__name__)

@app.route('/')
def default():
    return render_template('/templates/login.html')