import flask
from flask import request, jsonify, render_template
import json
import os
import secrets
import bcrypt

app = flask.Flask(__name__)

if not os.path.exists('config.json'):
    print("No config file found")
    with open('config.json', 'w') as f:
        f.write("{}")
    exit(1)

if not os.path.exists('users.json'):
    with open('users.json', 'w') as f:
        f.write("{}")
        users = {}
else:
    with open('users.json', 'r') as f:
        users = json.load(f)

with open('config.json', 'r') as f:
    config = json.load(f)

tokens = {}

def check_login(username, password):
    if not username or not password:
        return False, "Missing username or password"
    if username not in users:
        return False, "Incorrect username or password"
    if not bcrypt.checkpw(password.encode('utf-8'), users[username].encode('utf-8')):
        return False, "Incorrect username or password"
    return True, "Success"

def is_existing(user_name):
    if not isinstance(users, dict):
        return False
    return user_name in users

def add_user(user_name, psswd):
    users[user_name] = bcrypt.hashpw(psswd.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

#======== route ========

@app.route('/')
def home():
    return render_template('verification.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/login')
def default():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

#======== api route ========
@app.route("/api/login", methods=["POST", "OPTIONS"])
def api_login():
    if request.method == "OPTIONS":
        return '', 200

    try:
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "Missing data"}), 400
            
        username = data.get("username")
        password = data.get("password")
        
        ok, msg = check_login(username, password)
        if ok:
            token = secrets.token_hex(16)
            tokens[username] = token
            return jsonify({"status": "success", "token": token})
        else:
            if msg == "Incorrect password or username":
                return jsonify({"status": "error", "message": msg}), 401
            else:
                return jsonify({"status": "error", "message": msg}), 400

    except Exception as e:
        print(f"Erreur dans api_login: {e}")
        return jsonify({"status": "error", "message": "Internal error"}), 500
    
@app.route('/api/signup', methods=["POST", "OPTIONS"])
def api_signup():
    if request.method == "OPTIONS":
        return '', 200

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
        
    if is_existing(username):
        return jsonify({"status": "error", "message": "Utilisateur existe déjà"}), 409
    else:
        add_user(username, password)
        return jsonify({"status": "success", "message": "Utilisateur créé"}), 201

app.run(debug=True, port=config["port"], host="0.0.0.0")