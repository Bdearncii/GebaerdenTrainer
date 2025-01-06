
from flask import Blueprint, jsonify, request

signup_bp = Blueprint('signup', __name__)
login_bp = Blueprint('login', __name__)

users = {}

# Todo: Firebase Integration
@signup_bp.route('/signup', methods=['POST'])
def signup():
    # Empfange JSON-Daten vom Client
    data = request.get_json()

    # Benutzername und Passwort aus dem Request erhalten
    email=data.get('email')
    username = data.get('username')
    password = data.get('password')


    if username in users:
        # Benutzername exestiert bereits
        return jsonify({"error": "User already exists"}), 409

    # Registrierung erfolgreich
    users[username] = password
    return jsonify({"message": "Successfull SignUp"}), 201

# Todo: Firebase Integration
@login_bp.route('/login', methods=['POST'])
def login():
    # Empfange JSON-Daten vom Client
    data = request.get_json()

    # Überprüfen, ob Benutzername und Passwort im Request enthalten sind
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        # Erfolgreicher Login, sende JSON-Antwort mit Erfolg
        return jsonify({"message": f"Welcome, {username}!"}), 202
    else:
        # Ungültige Anmeldedaten, sende Fehlerantwort
        return jsonify({"error": "Invalid username or password"}), 401

