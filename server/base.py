from flask import Flask
from flask_cors import CORS
from routes.login import login_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(login_bp)

# um Flask zu starten, schreibt man in cmd: flask --debug run
if __name__ == '__main__':
    app.run(debug=True)
