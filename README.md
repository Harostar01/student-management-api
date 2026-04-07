# 🎓 Student Management API

A simple RESTful API built with Flask for managing student records.

---

## 🚀 Features
- Add a student
- View all students
- Update student details
- Delete a student
-  Uses SQLite database for persistent storage

---

## 🛠 Tech Stack
- Python
- Flask
- ## Sample Response

GET /students

[
  {
    "id": 1,
    "name": "Joshua",
    "age": 25
  }
]
-  SQLite (Database)

---

## 📌 API Endpoints

### GET all students
GET /students

### Add student
POST /students

Example JSON:
{
  "name": "Joshua",
  "age": 25
}

### Update student
PUT /students/<index>

### Delete student
DELETE /students/<index>

---

## ▶️ How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run the app:
python app.py

---

## 📂 Project Structure
- app.py → Main application
- routes.py → API routes
- models.py → Data storage

---

## 👨‍💻 Author
ARO JOSHUA OLAMILEKAN  
GitHub: https://github.com/Harostar01
