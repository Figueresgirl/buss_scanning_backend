
# buss_scanning_backend

BUSSCOLLAB AI-powered backend for scanning and managing construction materials from unstructured data (invoices, notes, field input).

## Overview

This backend powers the BUSSCOLLAB inventory tracking system by:

- Extracting materials and quantities using AI
- Converting raw text into structured JSON
- Storing inventory in AWS DynamoDB
- Providing API endpoints for inventory management

## Tech Stack

- FastAPI (Python backend)
- OpenAI API (AI extraction)
- AWS DynamoDB (NoSQL database)
- Boto3 (AWS SDK)
- Uvicorn (ASGI server)

##  Project Structure

buss_scanning_backend/
│
├── backend/
│   ├── app.py
│
│   ├── routes/
│   │   ├── scan.py
│   │   └── inventory.py
│
│   ├── services/
│   │   ├── llm_parser.py
│   │   └── db.py
│
├── .env
├── .gitignore
└── README.md

## Setup

### 1. Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/buss_scanning_backend.git
cd buss_scanning_backend

### 2. Install dependencies

```bash
python -m pip install fastapi uvicorn requests boto3 python-dotenv
```

---

### 3. Configure environment

Create `.env` file:

```
OPENAI_API_KEY=your_openai_key

AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key

DYNAMODB_TABLE=inventory_items
```

---

### 4. Run server

```bash
python -m uvicorn backend.app:app --reload
```

---

### 5. Open API

```
http://127.0.0.1:8000/docs
```

---

## Endpoints

### POST /scan

Extract materials from text.

### GET /inventory/list

Retrieve stored inventory.

## Current Status

* API running locally
* AI extraction working
* Inventory endpoint built
* DynamoDB connection pending credentials

## Next Steps

* Save scan results to database
* Build inventory add endpoint
* Normalize materials (key feature)
* Add authentication

##  Vision

BUSSCOLLAB enables construction teams to:

* Track materials across job sites
* Prevent duplicate purchases
* Reduce waste
* Increase profit margins

## 👤 Author

Thais Medina
Founder – BUSSCOLLAB

## ⚠️ Security

Do NOT upload `.env` to GitHub.

