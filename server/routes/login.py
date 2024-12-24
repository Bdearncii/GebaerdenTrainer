from flask import Blueprint, jsonify, request
from flask_cors import CORS

login_bp = Blueprint('login', __name__)
CORS(login_bp, resources={r"/signin": {"origins": "*"}})

users = []

# Todo: Logik verbessern + Firebase Integration
@login_bp.route('/signin', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    print("Username:", username)
    print("Password:", password)

    return jsonify({"message": "User registered successfully"}), 201
