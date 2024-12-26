from flask import Flask
from flask_cors import CORS
from blueprints.login.routes import login_bp

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.register_blueprint(login_bp)

if __name__ == '__main__':
    app.run(debug=True)
