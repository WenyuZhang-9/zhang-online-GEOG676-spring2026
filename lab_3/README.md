# Lab 3 - Object Oriented Programming (OOP)

This lab demonstrates the use of object-oriented programming in Python to calculate the area of different geometric shapes.

The program reads shape data from a text file, creates an object for each shape using classes, and prints the area of each shape.

---

## 📂Files in this repository

- `lab3.py`  
  Python script that defines shape classes, reads data from a text file, and computes areas.

- `shape.txt`  
  Input text file containing shape data (Rectangle, Circle, Triangle).

- `output.png`  
  Screenshot of the executed program and printed output.

---

## How it works

1. Shape data is read line-by-line from `shape.txt`.
2. A corresponding object (`Rectangle`, `Circle`, or `Triangle`) is created for each line.
3. All shape objects are stored in a list.
4. The program iterates through the list and prints the area of each shape.

---

## ▶️How to run

From the project directory, run:

```bash
python lab3.py
