# Object-Oriented Programming in Python – Introduction

---

## 🔹 What is Object-Oriented Programming (OOP)?
- OOP is a way of structuring programs so that **data** (attributes) and **behavior** (methods) are bundled into **objects**.  
- Instead of writing only **procedures/functions** (as in COBOL or C), we create **objects** that represent real-world entities.  

👉 Example: A **Bank Account** object can have:  
- Attributes → account number, balance  
- Methods → deposit, withdraw  

---

## 🔹 Why OOP?
- Makes code more **organized, reusable, and maintainable**.  
- Easier to model **real-world entities**.  
- Promotes **modularity** → large programs can be split into classes.  

---

## 🔹 Python as Multi-Paradigm
- Python is **multi-paradigm**: supports both **procedural** and **object-oriented** styles.  
- You can write small scripts in procedural style (like COBOL), or large systems in OOP style (like Java/C#).  

Example:
```python
# Procedural style
balance = 1000
def deposit(amount):
    global balance
    balance += amount

deposit(500)
print(balance)  # 1500
```

```python
# OOP style
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

account = BankAccount(1000)
account.deposit(500)
print(account.balance)  # 1500
```

---

## 🔹 Core OOP Concepts
Python supports the four pillars of OOP:
1. **Encapsulation** → Bundling data and methods.  
2. **Inheritance** → Reusing code across classes.  
3. **Polymorphism** → Same method behaves differently in different contexts.  
4. **Abstraction** → Hiding implementation details, exposing only essentials.  

---

## 🔹 COBOL / Java / C# Mapping
| Concept | COBOL | Java / C# | Python |
|---------|-------|-----------|--------|
| Program Style | Procedural only | Pure OOP (everything inside classes) | Both procedural + OOP |
| Data Structures | Records (FD, 01 LEVEL) | Classes with attributes | Classes with attributes |
| Behavior | PERFORM sections | Methods inside classes | Methods inside classes |
| Access Control | Not available | public/private/protected | Convention-based (`_var`, `__var`) |

---

## 💡 Exercises
1. Write a procedural Python program that manages a balance with deposit/withdraw functions.  
2. Rewrite the same program using a `BankAccount` class with `deposit` and `withdraw` methods.  
3. Compare the two styles and note which feels easier to extend with more features (like interest).  

---
