import firebase_admin
from flask import Blueprint, jsonify, request
from firebase_admin import db, credentials
import bcrypt
import os, json

with open(".env.json", "r") as file:
    config = json.load(file)


cred = credentials.Certificate(config)  # Credentials der Datenbank
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://gebaerdentrainer-default-rtdb.europe-west1.firebasedatabase.app"})  # Initializierung der Datenbank
ref = db.reference('/')

signup_bp = Blueprint('signup', __name__)
login_bp = Blueprint('login', __name__)

users = {}


# Todo: Firebase Integration
@signup_bp.route('/signup', methods=['POST'])
def signup():
    # Empfange JSON-Daten vom Client
    data = request.get_json()

    # Referenz auf die Datenbank und explizit auf die User-Tabelle
    user_ref = db.reference('users')

    # Benutzername und Passwort aus dem Request erhalten
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    password_hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    if username in users:
        # Benutzername exestiert bereits
        return jsonify({"error": "User already exists"}), 409

    # Registrierung erfolgreich

    # Hinzufügen des Users in die Datenbank
    dbdata = {"username": username, "password": password_hashed}
    user_ref.push(data)
    return jsonify({"message": "Successfull SignUp"}), 201


    # Code für tests ohne DB-Abhängigkeit
    # users[username] = password_hashed
    # return jsonify({"message": "Successfull SignUp"}), 201


# Todo: Firebase Integration
@login_bp.route('/login', methods=['POST'])
def login():
    # Empfange JSON-Daten vom Client
    data = request.get_json()

    # Referenz von Datenbank
    user_ref = db.reference('users')

    # Überprüfen, ob Benutzername und Passwort im Request enthalten sind
    username = data.get('username')
    password = data.get('password')

    user = user_ref.get(username)

    # Direkter Vergleich in der Datenbank
    if username == user['username'] and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        return jsonify({"message": f"Welcome, {username}!"}), 202
    else:
        return jsonify({"error": "Invalid username or password"}), 401

    # Code für tests ohne DB-Abhängigkeit
    # if username in users and bcrypt.checkpw(password.encode('utf-8'), users[username]):
    #     # Erfolgreicher Login, sende JSON-Antwort mit Erfolg
    #     return jsonify({"message": f"Welcome, {username}!"}), 202
    # else:
    #     # Ungültige Anmeldedaten, sende Fehlerantwort
    #     return jsonify({"error": "Invalid username or password"}), 401
