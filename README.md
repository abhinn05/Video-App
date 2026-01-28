# 📺 API-First Video App

[cite_start]A high-performance **React Native** mobile application powered by a **Flask** and **MongoDB** backend[cite: 7]. [cite_start]This project demonstrates a strict **thin-client architecture**, where all business logic and content abstraction are handled securely by the backend[cite: 5, 13].

---

## 🏗️ System Architecture (Non-Negotiable)
[cite_start]This project follows a strict separation of concerns to ensure the mobile app remains a "thin client"[cite: 6, 13]:
* [cite_start]**Mobile App (React Native)**: Handles rendering, JWT storage, and user actions only [cite: 14-18].
* [cite_start]**Flask API**: Manages authentication, video logic, and source abstraction [cite: 48-49].
* [cite_start]**MongoDB**: Stores user records and video metadata[cite: 83].



---

## 🔐 The "YouTube Twist" (Security Implementation)
[cite_start]To meet security requirements, the app **never** directly interacts with YouTube URLs[cite: 10, 44]. 
* [cite_start]**Abstraction**: The backend hides raw YouTube IDs and provides a masked `playback_token` or stream proxy [cite: 72-78].
* [cite_start]**Security**: This prevents source exposure and ensures the app is useless without the backend[cite: 98].

---

## 🛠️ Tech Stack
* [cite_start]**Frontend**: React Native (Thin Client) [cite: 11]
* [cite_start]**Backend**: Flask (API-First logic) [cite: 48]
* [cite_start]**Database**: MongoDB [cite: 83]
* [cite_start]**Auth**: JWT (JSON Web Tokens) [cite: 51]

---

## 🚀 Installation & Setup

### 1. Backend Setup (Flask)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
### 2. Mobile App Setup (React Native)
```bash
cd mobile
npm install
npx expo start
```
## 📋 API Reference

### Authentication Endpoints
| Method | Endpoint | Purpose |
| :--- | :--- | :--- |
| `POST` | `/auth/signup` | [cite_start]Register a new user with hashed passwords [cite: 53, 54] |
| `POST` | `/auth/login` | [cite_start]Authenticate user and return a JWT  |
| `GET` | `/auth/me` | [cite_start]Return the current user's profile  |
| `POST` | `/auth/logout` | [cite_start]Invalidate the token or mock logout logic  |

---

## 🤖 AI Transparency & Reflections
[cite_start]As per the submission requirements[cite: 122, 123]:

### Where AI Helped
* [cite_start]**Boilerplate Generation**: AI assisted in scaffolding the initial Flask routes and React Native component structures to meet the 24-hour deadline[cite: 1].
* [cite_start]**Schema Design**: Helped quickly map the User and Video models to MongoDB-compatible JSON formats [cite: 83-96].

### Where AI Was Wrong & Manual Fixes
* **YouTube Logic**: AI initially suggested direct YouTube URLs. [cite_start]I manually refactored this to implement the **Video Wrapper Strategy** to ensure no raw YouTube links are exposed to the frontend[cite: 44, 45].
* **State Management**: AI suggested complex Redux logic; [cite_start]I manually simplified this to a "Thin Client" model using local state and secure storage to keep the frontend logic-free[cite: 13].

---

## 🏁 Submission Checklist
* GitHub Repository (Frontend + Backend)
* `.env.example` included
* Setup Instructions provided 
* 3-5 Minute Loom Video 

---

## 👤 Author
**Abhinn**
*IIT Mandi*
