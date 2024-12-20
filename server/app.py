from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user data
users = {
    "user1": "password1",
    "user2": "password2",
    'test1': 'test'
}

@app.route('/login', methods=['POST'])
def login():
    # Empfange JSON-Daten vom Client
    data = request.get_json()

    # Überprüfen, ob Benutzername und Passwort im Request enthalten sind
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        # Erfolgreicher Login, sende JSON-Antwort mit Erfolg
        return jsonify({"message": f"Welcome, {username}!"}), 200
    else:
        # Ungültige Anmeldedaten, sende Fehlerantwort
        return jsonify({"error": "Invalid username or password"}), 401

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
