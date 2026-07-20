# 🏛️ SmartGov AI

> AI-Powered Government Document Verification System

SmartGov AI is an intelligent government service platform that automates document verification using Artificial Intelligence. The system verifies uploaded documents, extracts text using OCR, detects faces, calculates a trust score, and generates a professional verification report.

---

# 🚀 Features

- 📄 OCR-based Document Text Extraction
- 👤 Face Detection using OpenCV YuNet
- 🧠 AI Trust Score Calculation
- 📑 Automatic Document Parsing
- 📊 Officer Dashboard
- 📃 PDF Verification Report Generation
- 🌐 Responsive Government Portal
- 🔒 Secure File Upload
- ⚡ FastAPI REST API
- 🎨 Modern HTML/CSS/JavaScript Frontend

---

# 🛠️ Tech Stack

### Backend

- FastAPI
- Python 3.11
- OpenCV
- EasyOCR
- PyMuPDF
- ReportLab
- Pydantic
- Uvicorn

### Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap

### AI Components

- EasyOCR
- OpenCV YuNet Face Detection
- Trust Score Engine
- Document Parser

---

# 📂 Project Structure

```
SmartGov-AI
│
├── backend
│   ├── api
│   ├── services
│   ├── database
│   ├── reports
│   ├── uploads
│   ├── models
│   ├── main.py
│   ├── requirements.txt
│   └── runtime.txt
│
├── frontend
│   ├── assets
│   ├── index.html
│   ├── verification.html
│   ├── officer.html
│   ├── analytics.html
│   ├── ai_assistant.html
│   └── services.html
│
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/SmartGov-AI.git

cd SmartGov-AI
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
cd backend

pip install -r requirements.txt
```

---

# ▶️ Run Project

```bash
cd backend

uvicorn main:app --reload
```

Open your browser

```
http://127.0.0.1:8000
```

---

# 🌐 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Home Page |
| GET | /verification | Verification Page |
| GET | /officer | Officer Dashboard |
| GET | /analytics | Analytics Dashboard |
| GET | /assistant | AI Assistant |
| GET | /services | Government Services |
| POST | /api/verify | Verify Uploaded Documents |

---

# 📄 Verification Workflow

1. Upload Government Document
2. Upload Selfie
3. OCR extracts document text
4. Document Parser identifies details
5. Face Detection verifies identity
6. Trust Score is calculated
7. PDF Verification Report is generated
8. Verification result is returned

---

# 📊 AI Modules

- OCR Service
- Face Detection
- Trust Score Calculation
- Document Parsing
- PDF Report Generation

---

# 📷 Screenshots

Add screenshots here

```
Home Page

Verification Page

Officer Dashboard

Analytics Dashboard

Generated PDF Report
```

---

# 🚀 Deployment

### Render

Root Directory

```
backend
```

Build Command

```bash
pip install -r requirements.txt
```

Start Command

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

# 📦 Requirements

- Python 3.11+
- FastAPI
- EasyOCR
- OpenCV
- PyMuPDF
- ReportLab
- Uvicorn

---

# 🔮 Future Enhancements

- MongoDB Atlas Integration
- AI Forgery Detection
- Face Liveness Detection
- Aadhaar Verification
- Passport Verification
- QR Code Validation
- Digital Signature Verification
- Officer Authentication
- Email Notifications
- Multi-language OCR

---

# 👩‍💻 Developer

**Trisha Hingu**

B.Sc. Information Technology

Vanita Vishram Women's University

📧 Email: trishahingu2406@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/trisha-hingu-630252341/

💻 GitHub: https://github.com/trishahingu

---

# 📜 License

This project is developed for educational, research, and hackathon purposes.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
