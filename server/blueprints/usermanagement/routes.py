import firebase_admin
from flask import Blueprint, jsonify, request
from firebase_admin import db, credentials
import bcrypt

cred = credentials.Certificate("credentials.json")  # Credentials der Datenbank
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

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    if username in users:
        # Benutzername exestiert bereits
        return jsonify({"error": "User already exists"}), 409

    # Registrierung erfolgreich
    users[username] = password

    # Hinzufügen des Users in die Datenbank
    dbdata = {"username": username, "password": hashed}
    user_ref.push(data)
    return jsonify({"message": "Successfull SignUp"}), 201


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
    if username == user['username'] and bcrypt.checkpw(password, user['password']):
        return jsonify({"message": f"Welcome, {username}!"}), 202
    else:
        return jsonify({"error": "Invalid username or password"}), 401

    # if username in users and users[username] == password:
    #     # Erfolgreicher Login, sende JSON-Antwort mit Erfolg
    #     return jsonify({"message": f"Welcome, {username}!"}), 202
    # else:
    #     # Ungültige Anmeldedaten, sende Fehlerantwort
    #     return jsonify({"error": "Invalid username or password"}), 401
