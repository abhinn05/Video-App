from datetime import datetime

# User Model [cite: 84-89]
def create_user_doc(name, email, password_hash):
    return {
        "name": name,
        "email": email,
        "password_hash": password_hash,
        "created_at": datetime.utcnow()
    }

# Video Model [cite: 90-96]
def create_video_doc(title, description, youtube_id, thumbnail_url):
    return {
        "title": title,
        "description": description,
        "youtube_id": youtube_id,
        "thumbnail_url": thumbnail_url,
        "is_active": True
    }