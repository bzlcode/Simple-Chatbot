# 🤖 AI Chatbot with python

A web-based AI chatbot built using **Python**, **Flask**, and **HTML/CSS/JavaScript frontend**.  
The application provides a simple chat interface in the browser, sends user queries to a Flask backend, and returns AI-generated responses.

This project is fully **code-driven** and focuses on understanding backend development, frontend–backend communication, and AI API integration.

---

## 🚀 Features

- Web-based chat interface (HTML, CSS, JavaScript)
- Flask backend for request handling
- AI-powered responses (groq)
- REST API communication between UI and backend
- Groq API is used for generating responses
(Can be replaced with Gemini, OpenAI, etc., by modifying ai_engine.py)

## 📂 Project Structure

```Simple-Chatbot/

├── src/
│   ├── main.py
│   └── ai_engine.py
├── templates/
│   ├── chat.html
│   └── summarizer.html
├── keys.env.example
├── .gitignore
└── README.md

```

## 🧱 Architecture Overview

Web Browser (web)
↓
HTTP request (POST)
↓
Flask Backend
↓
AI response
↓
Response rendered back to UI

---

## 🛠️ Tech Stack

- **Language**: Python 3
- **Backend Framework**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **AI Model**: groq (can be changed)
- **HTTP Client**: Requests
- **Environment Management**: python-dotenv

---

## Install dependencies

pip install -r requirements.txt

## Running the Application

python src/main.py
