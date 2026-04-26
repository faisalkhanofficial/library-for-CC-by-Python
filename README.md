# 📚 Library Management System

## 📌 Overview

This is a **menu-driven Library Management System** built in Python using a **modular (package-based) architecture**.
The project allows users to manage books, issue and return them, and automatically calculates fines for late returns.

---

## 🚀 Features

* 📖 View all books with availability status
* ➕ Add new books to the library
* 📥 Issue books with student name and number of days
* 📤 Return books with automatic fine calculation
* 💰 Progressive fine system for late returns
* 🔁 Continuous menu using `while True` loop
* 🧩 Well-structured code with separate files for each functionality

---

## 🗂️ Project Structure

```text
Library_Project/
│── main.py
│
│── services/
│     ├── add_book_service.py
│     ├── issue_book_service.py
│     ├── return_book_service.py
│     ├── fine_service.py
│
│── data/
│     └── library_data.py
│
│── utils/
│     └── helper.py
│
│── README.md
```

---

## ⚙️ Functionality

### 📖 Show Books

Displays all books along with their availability status (Available / Issued).

### ➕ Add Book

Allows adding a new book to the library database.

### 📥 Issue Book

* Takes book name, student name, and number of days
* Stores issue date and marks the book as unavailable

### 📤 Return Book

* Calculates how many days the book was used
* Applies fine if returned late
* Updates book availability

---

## 💰 Fine Policy

The fine increases progressively for each extra day:

* Day 1 → ₹10
* Day 2 → ₹20
* Day 3 → ₹30
* and so on...

**Formula used:**

```text
Fine = 10 × (1 + 2 + 3 + ... + extra_days)
```

---

## ▶️ How to Run

### Step 1: Open terminal and go to project folder

```bash
cd Library_Project
```

### Step 2: Run the program

```bash
python main.py
```

---

