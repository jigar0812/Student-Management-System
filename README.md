# Student Management System

A simple web-based Student Management System built with **Python, Flask, SQLite, HTML and CSS**. It was developed for a Software Engineering Internship and demonstrates CRUD operations, validation, search, unit testing, debugging, code review and refactoring.

## Features
- Add, view, edit and delete students
- Search by name, roll number, email or course
- Input validation and duplicate roll-number prevention
- SQLite database
- Modular service/database structure
- Unit tests with `unittest`
- Parameterized SQL queries

## Setup

```bash
git clone https://github.com/YOUR-USERNAME/Student-Management-System.git
cd Student-Management-System
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

macOS/Linux:
```bash
source venv/bin/activate
```

Install and run:
```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## Tests
```bash
python -m unittest discover -s tests -v
```

## Structure
```text
app.py
config.py
requirements.txt
README.md
CODE_REVIEW.md
database/database.py
models/student.py
services/student_service.py
templates/
static/style.css
tests/test_student.py
```

## Code Review & Refactoring
The project was reviewed for long functions, duplicate database logic, poor naming, mixed responsibilities, limited validation, hard-coded values and insufficient documentation. Refactoring separated routes, database access and business logic, centralized validation, improved naming and added unit tests.

## Internship Relevance
This repository demonstrates software module development, database integration, testing, debugging, code review, refactoring, documentation and Git/GitHub version control.

**Author:** Jigar Yadav  
**Role:** Software Engineering Trainee
