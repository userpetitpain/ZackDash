import flask
from flask import request, jsonify, render_template
import json
import os

app = flask.Flask(__name__)

if not os.path.exists('config.json'):
    print("No config file found")
    with open('config.json', 'w') as f:
        f.write("{}")
    exit(1)

with open('config.json', 'r') as f:
    config = json.load(f)

@app.route('/')
def default():
    return render_template('login.html')

app.run(debug=True, port=config["port"], host="0.0.0.0")