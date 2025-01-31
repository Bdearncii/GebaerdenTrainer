import sys
import os
import firebase_admin
from flask import Flask, request, jsonify
from flask_cors import CORS
from blueprints.usermanagement.routes import signup_bp, login_bp # 'server' muss in vor dem Umsetzen in die Prokutionsumgebung gelöscht werden (Übergangslösung)
from firebase_admin import db, credentials

cred = credentials.Certificate('credentials.json') # Credentials der Datenbank
ref = db.reference('/')

app = Flask(__name__)
CORS(app, supports_credentials=True)


app.register_blueprint(signup_bp)
app.register_blueprint(login_bp)


@app.route('/add_user', methods=['POST'])
def add_user_route():
    params = request.get_json()
    user_ref = db.reference('users')
    #user_count = user_ref.get() or 0  // Geben wir dem User eine ID? 
    #user_count += 1
    data={"username":params['user'],"email":params['email'],"password":params['password'],}
    user_ref.push(data)
    return jsonify({"message": "User added successfully"}), 201 


# @app.route('/get_user/<id>', methods=['GET'])
# def get_user_route():
#      params = request.get_json()
#      user_ref = db.reference('users')
#      if params.username == user_ref.get():
#             if user_ref




# @app.route('/add_progress',methods=['POST'])
# def add_progress_route():
#     params = request.get_json()
#     progress_ref = db.reference('progress') 
#     add_progress(data['user_id'], data['sprache'], data['completion_date'])
#     return jsonify({"message": "Progress added successfully"}), 201

# Wie sollen wir Progress speichern? Intern beim User?



@app.route('/add_video', methods=['POST'])
def add_video_route():
    params = request.get_json()
    video_ref = db.reference('videos')
    data={"Sprache": params['lang'], "URL": params['url'], "Description": params['description']}
    video_ref.push(data)
    return jsonify({"message": "Video added successfully"}), 201


@app.route('/get_video/<description>', methods=['GET'])
def get_video_route(video_description):
    params = request.get_json()
    video_ref = db.reference('videos')
    for video in video_ref: # durch die individuellen Videos werden durchgegangen
        if video['description'] == params['video_description']:
                return jsonify(video)

    return jsonify({"message": "Video does not exist!"})
            




if __name__ == '__main__':
    app.run(debug=True)
