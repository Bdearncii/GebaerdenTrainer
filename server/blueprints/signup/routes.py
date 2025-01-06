from contextlib import nullcontext

from flask import Blueprint, jsonify, request
from flask_cors import CORS

signup_bp = Blueprint('login', __name__)

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


    if email in users:
        # Benutzername exestiert bereits
        return jsonify({"error": "User already exists"}), 409

    # Registrierung erfolgreich
    users[email] = username, password
    return jsonify({"message": "Successfull SignUp"}), 201

