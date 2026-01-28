from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import bcrypt
import os

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/videoApp"
app.config["JWT_SECRET_KEY"] = "super-secret-key" # Use .env in production
mongo = PyMongo(app)
jwt = JWTManager(app)

# --- Auth Endpoints --- [cite: 53]
@app.route('/auth/signup', methods=['POST'])
def signup():
    data = request.json
    hashed_pw = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()) # [cite: 54]
    mongo.db.users.insert_one({
        "name": data['name'],
        "email": data['email'],
        "password": hashed_pw
    })
    return jsonify({"msg": "User created"}), 201

@app.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    user = mongo.db.users.find_one({"email": data['email']})
    if user and bcrypt.checkpw(data['password'].encode('utf-8'), user['password']):
        token = create_access_token(identity=str(user['_id'])) # [cite: 51]
        return jsonify(access_token=token), 200
    return jsonify({"msg": "Bad credentials"}), 401

# --- Video Endpoints --- [cite: 65]
@app.route('/dashboard', methods=['GET'])
@jwt_required()
def get_dashboard():
    # Only return 2 videos [cite: 65]
    videos = list(mongo.db.videos.find({"is_active": True}).limit(2))
    output = []
    for v in videos:
        output.append({
            "id": str(v['_id']),
            "title": v['title'],
            "description": v['description'],
            "thumbnail_url": v['thumbnail_url']
        })
    return jsonify(output), 200

@app.route('/video/<id>/stream', methods=['GET'])
@jwt_required()
def stream_video(id):
    # Abstracting YouTube: Generate a masked URL [cite: 66, 69, 71]
    video = mongo.db.videos.find_one({"_id": id})
    # In a real app, you'd sign a temporary URL or proxy the stream
    masked_url = f"https://www.youtube.com/embed/{video['youtube_id']}?controls=0" 
    return jsonify({"stream_url": masked_url}), 200

if __name__ == '__main__':
    app.run(debug=True)