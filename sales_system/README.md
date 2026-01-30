# Sales System – Python Console Application

This project implements a **console-based sales management system** developed in Python.  
It simulates the core logic of a small point-of-sale system, focusing on **clean structure, data persistence, and logical flow**, rather than graphical interfaces.

The project is part of my academic and practical training in **Computer Science and programming fundamentals**.

---

## 📌 Project Description

The system allows users to:

- Manage a list of products
- Search products by name
- Register sales transactions
- Persist inventory and sales data using JSON files
- Generate basic sales reports

The application follows a **modular design**, separating responsibilities across different files to improve readability, maintainability, and scalability.

---

## 🧱 Project Structure
sales-system/
│
├── main.py
│ # Entry point of the application (menu and user interaction)
│
├── modulos/
│ ├── recursos.py
│ │ # Product management, sales processing, JSON persistence
│ │
│ └── reportes.py
│ # Sales reports and aggregated summaries
│
├── data/
│ ├── products.json
│ │ # Persistent product inventory
│ │
│ └── sales.json
│ # Persistent sales records
│
└── README.md


---

## ⚙️ Features

- Menu-driven console interface
- Product listing and search
- Sales processing with stock validation
- Persistent storage using JSON files
- Automatic inventory updates after each sale
- Sales report with total revenue calculation

---

## 🧠 Concepts Applied

- Modular programming
- File handling (JSON persistence)
- Data structures (dictionaries and lists)
- Input validation and error handling
- Separation of concerns
- Structured problem-solving

---

## 🧪 Technologies Used

- Python 3
- Standard Python libraries:
  - `json`
  - `os`
  - `datetime`
