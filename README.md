# 🚀 Task API – CRUD Assignment

> A lightweight RESTful Task Management API built with **FastAPI** as part of the **FlyRank Backend AI Engineering Internship** assignment.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![REST API](https://img.shields.io/badge/REST-API-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

---

## 📖 Overview

This project is a simple **Task Management REST API** implementing complete **CRUD (Create, Read, Update, Delete)** functionality using **FastAPI**.

The application stores tasks **in memory**, making it lightweight and easy to understand while focusing on REST principles, request validation, and proper HTTP status codes.

> **Note:** Since data is stored in memory, all tasks are lost when the server restarts.

---

# ✨ Features

- ✅ Create new tasks
- 📋 Retrieve all tasks
- 🔍 Retrieve a task by ID
- ✏️ Update existing tasks
- 🗑️ Delete tasks
- ✔️ Input validation
- 📄 Automatic Swagger documentation
- 🚀 FastAPI-based REST API

---

# 🛠️ Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Uvicorn**

---

# 📂 Project Structure

```text
.
├── main.py
├── README.md
└── requirements.txt
```

---

# 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API information |
| GET | `/health` | Health check |
| GET | `/tasks` | Retrieve all tasks |
| GET | `/tasks/{id}` | Retrieve a task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

---

# 🚀 Running the Project

## 1. Clone the repository

```bash
git clone <your-repository-url>
cd <repository-name>
```

## 2. Install dependencies

```bash
pip install fastapi uvicorn
```

or

```bash
pip install -r requirements.txt
```

## 3. Start the development server

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://localhost:8000
```

---

# 📚 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```
http://localhost:8000/docs
```

### ReDoc

```
http://localhost:8000/redoc
```

---

# 🧪 Testing the API

## Create a Task

```bash
curl -X POST http://localhost:8000/tasks \
-H "Content-Type: application/json" \
-d '{"title":"Learn FastAPI"}'
```

---

## Retrieve All Tasks

```bash
curl http://localhost:8000/tasks
```

---

## Retrieve a Task

```bash
curl http://localhost:8000/tasks/1
```

---

## Update a Task

```bash
curl -X PUT http://localhost:8000/tasks/1 \
-H "Content-Type: application/json" \
-d '{"done": true}'
```

---

## Delete a Task

```bash
curl -X DELETE http://localhost:8000/tasks/1
```

---

# 📦 Example Response

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "done": false
}
```

---

# 📊 HTTP Status Codes

| Status Code | Meaning |
|--------------|---------|
| 200 | Request successful |
| 201 | Resource created |
| 204 | Resource deleted successfully |
| 400 | Invalid request or input |
| 404 | Resource not found |

---

# 📷 Screenshots

### Swagger UI

<img width="1920" height="1080" alt="{71355D6F-D949-40FC-BC58-9514F6F523A1}" src="https://github.com/user-attachments/assets/401d508a-9548-4d99-9fdc-5d6e4b39922b" />


---

# 🎯 Learning Outcomes

Through this project I gained hands-on experience with:

- Building REST APIs using FastAPI
- CRUD application development
- HTTP methods and REST conventions
- Request validation
- Proper HTTP status codes
- Automatic API documentation with Swagger
- Working with in-memory data storage
- Testing APIs using Swagger UI and `curl`

---

# 🤖 AI vs My Implementation

As part of the assignment, I compared my implementation with an AI-generated solution.

### What I implemented better

- Proper validation for empty task titles
- Appropriate HTTP status codes
- Clearer API behavior

### What the AI implemented better

- More concise implementation
- Cleaner comments and structure

### Improvements I identified

- Explicitly specifying DELETE should return **204 No Content**
- Auto-incrementing task IDs

### Key Takeaway

> Building the API first made it much easier to evaluate AI-generated code critically. Good prompts produce better AI outputs, but understanding the fundamentals is what allows you to judge their quality.

---

# 👨‍💻 Author

**Hasib Md Turjo**

Built as part of the **FlyRank Backend AI Engineering Internship** assignment.

---
