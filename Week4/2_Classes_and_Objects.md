# Classes and Objects in Python

---

## 🔹 What is a Class?
- A **class** is a blueprint for creating objects.  
- It defines **attributes** (data) and **methods** (behavior).  
- Think of it like a **template** or **record layout** in COBOL, or a **class** in Java/C#.  

---

## 🔹 What is an Object?
- An **object** is an **instance** of a class.  
- Each object has its own copy of attributes defined in the class.  

Example:
```python
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print(f"Account {self.account_number}, Balance: {self.balance}")

# Creating objects
acc1 = BankAccount("A1001", 500)
acc2 = BankAccount("A1002", 1000)

acc1.display()  # Account A1001, Balance: 500
acc2.display()  # Account A1002, Balance: 1000
```

---

## 🔹 The `__init__` Method
- Special method that runs when an object is created.  
- Initializes object attributes (like a constructor in Java/C#).  

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp = Employee("Alice", 7000)
print(emp.name, emp.salary)  # Alice 7000
```

---

## 🔹 Adding Methods
- Methods define behavior of objects.  
- First parameter of methods is always `self` → refers to the object itself.  

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee {self.name}, Salary: {self.salary}")

emp = Employee("Bob", 8000)
emp.display()  # Employee Bob, Salary: 8000
```

---

## 🔹 Updating Attributes
- You can update attributes directly or via methods.  

```python
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

account = BankAccount("A2001", 500)
account.deposit(200)
account.withdraw(100)
print(account.balance)  # 600
```

---

## 🔹 COBOL / Java / C# Mapping
| Concept | COBOL | Java / C# | Python |
|---------|-------|-----------|--------|
| Class | No classes, only RECORDS in FILE SECTION | `class Employee {}` | `class Employee:` |
| Object | Not applicable | `Employee emp = new Employee()` | `emp = Employee()` |
| Constructor | Not applicable | `public Employee(...) {}` | `def __init__(...)` |
| Methods | PERFORM paragraphs | `emp.display()` | `emp.display()` |

---

## 💡 Exercises
1. Create a `Car` class with attributes `brand` and `model`, and a method to display details.  
2. Create two `Student` objects with attributes `name` and `marks`. Write a method to check if a student has passed (marks >= 40).  
3. Extend the `BankAccount` class to include a method `check_balance()` that prints the current balance.  

---
