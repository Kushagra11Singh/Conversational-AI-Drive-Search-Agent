# Conversational AI Drive Search Agent

An AI-powered conversational assistant that helps users search, filter, and discover files from a designated Google Drive folder using natural language queries.

## Live Demo
Frontend (Streamlit): https://conversational-ai-drive-search-agent-b3ztxxtnybedjmfsmzvhr5.streamlit.app

Backend API (Render): https://conversational-ai-drive-search-agent.onrender.com/docs

GitHub Repository:
https://github.com/Kushagra11Singh/Conversational-AI-Drive-Search-Agent

---

## Problem Statement

This project was built as part of the TailorTalk assignment.

The goal was to create a conversational AI agent capable of:

- Understanding natural language search queries
- Searching files inside Google Drive
- Filtering by:
  - file name
  - partial name
  - file type
  - modified date
  - document content intent
- Returning relevant file results in a conversational interface

Example queries:

- Find all pdf reports
- Show me spreadsheets
- Find invoices from last week
- Find files containing marketing strategy

---

## Tech Stack

### Backend
- FastAPI
- Python
- Google Drive API
- LangChain
- Groq LLM API

### Frontend
- Streamlit

### Deployment
- Render (Backend)
- Streamlit Cloud (Frontend)

---

## Architecture Flow

User Query
→ Streamlit Chat UI
→ FastAPI Backend
→ LLM converts natural language into Google Drive query
→ Google Drive API searches files
→ Results returned to user

---

## Features

### Natural Language Search
Users can ask queries in plain English.

Example:
"Find all pdf reports"

---

### Google Drive Query Translation
The LLM converts user queries into valid Google Drive API `q` parameters.

Example:

User:
Find pdf reports

Generated query:
mimeType='application/pdf' and name contains 'report'

---

### Google Drive File Discovery
Searches files using:

- file name
- partial match
- mime type
- modified date

---

### Conversational UI
Simple chat interface built with Streamlit.

---

## Project Structure

```bash
tailortalk-drive-search-agent/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── services/
│   │   ├── tools/
│   │   └── utils/
│   │
│   ├── requirements.txt
│
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│
└── README.md
