# Simple AI Chatbot (School FAQ Assistant)

A beginner-level AI-powered chatbot built using Python and Flask.  
The chatbot answers predefined school-related FAQs and uses an AI fallback for unknown queries.

---

## 📌 Project Objective

To develop a simple, rule-based chatbot integrated with an AI API that can:

- Answer common school-related questions
- Handle unknown queries intelligently using AI
- Demonstrate core chatbot concepts (intents, preprocessing, fallback)

---

## 🧠 Features

- Rule-based FAQ handling using `intents.json`
- AI-powered fallback response (Google Gemini API)
- Text preprocessing (lowercase, symbol removal)
- Simple web-based chat interface
- Flask backend with REST API
- Beginner-friendly and extensible design

---

## 🛠️ Tech Stack

**Backend**

- Python
- Flask

**Frontend**

- HTML
- CSS
- JavaScript

**AI**
- Google Gemini API (Gemini-2.5-flash)

---

## 📂 Project Structure

```
Simple AI Chatbot/
│── app.py # Main Flask application
│── intents.json # Predefined questions and responses
│── requirements.txt # Python dependencies
│── README.md # Project documentation
├── .env # Environment variables
├── .gitignore # Git ignore file
│
├── templates/
│ └── index.html # Chat UI
│
├── static/
│ └── style.css # UI styling
│ └── script.js # UI script
```
