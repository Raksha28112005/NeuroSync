🧠 NeuroSync
AI Cognitive Overload Detection & Smart Intervention System

NeuroSync is an AI-powered prototype system that detects cognitive overload in real time using facial presence detection and generates a stress score with smart alerts.

This project demonstrates how AI + Edge Computing can help prevent burnout and improve productivity.

🚀 Project Overview

NeuroSync monitors:

Webcam facial detection

Behavioral interaction patterns (future scope)

Generates Stress Score (0–100)

Triggers smart break alerts

This prototype uses:

Python (FastAPI)

OpenCV

React.js

Axios

📁 Project Structure
NeuroSync/
│
├── backend/
│   ├── main.py
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   ├── package.json
│
├── .gitignore
└── README.md
⚙️ System Requirements

Python 3.10+

Node.js (LTS)

Git

VS Code (Recommended)

🖥️ Backend Setup (FastAPI + OpenCV)
Step 1: Navigate to backend folder
cd backend
Step 2: Install required packages
pip install fastapi uvicorn opencv-python
Step 3: Run the backend server
uvicorn main:app --reload
Expected Output:
Uvicorn running on http://127.0.0.1:8000
Application startup complete.
Test API in Browser

Open:

http://127.0.0.1:8000/stress
Example Output:
{
  "stress_score": 67
}

The stress score updates dynamically.

🌐 Frontend Setup (React Dashboard)
Step 1: Navigate to frontend folder
cd frontend
Step 2: Install dependencies
npm install
npm install axios
Step 3: Start React app
npm start
Expected Output:

Browser opens automatically at:

http://localhost:3000

Dashboard displays:

Live Cognitive Stress Score

Color indicator (Green / Red)

Alert message if stress > 75

📊 Input & Output Explanation
🎥 Input

Webcam video feed

Facial detection using OpenCV Haar Cascade

🧠 Processing

If face detected → Stress Score = Random (40–90)

If no face → Stress Score = Random (10–40)

📤 Output

Stress Score (0–100)

Break Alert if score > 75

Color-coded dashboard display

🔌 API Endpoint
GET /stress

Returns current stress score.

Example:

GET http://127.0.0.1:8000/stress

Response:

{
  "stress_score": 58
}
🧠 Architecture Overview

Input Layer

Webcam

AI Processing Layer

Face Detection Engine

Stress Score Generator

Backend API Layer

FastAPI

Frontend Layer

React Dashboard

Deployment Layer (Future Scope)

AMD Ryzen AI Edge Devices

Cloud Integration

💡 AMD Integration (Scalable Design)

NeuroSync is designed for:

AMD Ryzen AI for real-time edge inference

AMD EPYC processors for scalable backend computation

AMD ROCm for GPU-accelerated model training

🔮 Future Enhancements

Real emotion detection using CNN models

Typing behavior analytics

Eye strain detection

AI-based workload adaptation

Corporate analytics dashboard
