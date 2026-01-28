import bcrypt
from flask_jwt_extended import create_access_token

def hash_password(password):
    # Passwords must be hashed
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def generate_token(user_id):
    # Use JWT authentication
    return create_access_token(identity=str(user_id))