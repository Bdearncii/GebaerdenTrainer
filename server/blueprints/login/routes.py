from contextlib import nullcontext

from flask import Blueprint, jsonify, request
from flask_cors import CORS

login_bp = Blueprint('login', __name__)

users = {}

# Todo: Firebase Integration
@login_bp.route('/signup', methods=['POST'])
def signup():
    # Empfange JSON-Daten vom Client
    data = request.get_json()

    # Benutzername und Passwort aus dem Request erhalten
    username = data.get('username')
    password = data.get('password')

    if username in users:
        # Benutzername exestiert bereits
        return jsonify({"error": "Username already exists"}), 409

    # Registrierung erfolgreich
    users[username] = password
    return jsonify({"message": "Successfull SignUp"}), 201

