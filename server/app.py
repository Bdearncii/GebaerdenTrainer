import sys
import os
#Working directory wird auf den Übergeordnetenordner von Server geändert.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, request, jsonify
from flask_cors import CORS
from server.blueprints.signup.routes import signup_bp
from database.models import add_user, get_user_by_username, add_progress, get_progress_by_user, add_video, get_video_by_description

app = Flask(__name__)
CORS(app, supports_credentials=True)


app.register_blueprint(signup_bp)

@app.route('/add_user', methods=['POST'])
def add_user_route():
    data = request.get_json()
    add_user(data['username'], data['email'], data['password'])
    return jsonify({"message": "User added successfully"}), 201 


@app.route('/get_user/<username>', methods=['GET'])
def get_user_route(username):
    user = get_user_by_username(username)
    if user:
        return jsonify({"userid": user[0],
                        "username": user[1],
                        "email": user[2]
        })
    else:
        return jsonify({"message": "User not found"}),404


@app.route('/add_progress',methods=['POST'])
def add_progress_route():
    data = request.get_json()
    add_progress(data['user_id'], data['sprache'], data['completion_date'])
    return jsonify({"message": "Progress added successfully"}), 201


@app.route('/get_progress/<user_id>', methods=['GET'])
def get_progress_route(user_id):
    progress = get_progress_by_user(user_id)
    return jsonify(progress)



@app.route('/add_video', methods=['POST'])
def add_video_route():
    data = request.get_json()
    add_video(data['fach'], data['video_url'], data['video_description'])
    return jsonify({"message": "Video added successfully"}), 201


@app.route('/add_video/<description>', methods=['POST'])
def get_video_route(video_description):
    video = get_video_by_description(video_description)
    return jsonify(video)


if __name__ == '__main__':
    app.run(debug=True)
