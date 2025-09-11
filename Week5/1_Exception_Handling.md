# Exception Handling in Python

---

## 🔹 What is an Exception?
- An **exception** is an error that occurs during program execution.  
- Instead of stopping the entire program, Python allows us to **handle errors gracefully**.  

👉 Example: Division by zero, file not found, invalid input.  

---

## 🔹 Why Exception Handling?
- Prevents program crashes.  
- Provides user-friendly error messages.  
- Makes code more robust and reliable.  

---

## 🔹 Basic `try-except`
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")
```

Output:
```
You cannot divide by zero!
```

---

## 🔹 Catching Multiple Exceptions
```python
try:
    num = int("abc")  # ValueError
except ZeroDivisionError:
    print("Division by zero error")
except ValueError:
    print("Invalid number format")
```

---

## 🔹 Using `else` and `finally`
- `else`: runs if no exception occurs.  
- `finally`: always runs (cleanup code).  

```python
try:
    f = open("example.txt", "r")
    data = f.read()
except FileNotFoundError:
    print("File not found")
else:
    print("File read successfully")
finally:
    print("Closing file (if open)")
```

---

## 🔹 Raising Exceptions
Use `raise` to throw an exception manually.  

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

try:
    new_balance = withdraw(1000, 2000)
except ValueError as e:
    print("Error:", e)
```

---

## 🔹 Custom Exceptions
Define your own exception classes.  

```python
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Balance too low!")
    return balance - amount

try:
    withdraw(500, 1000)
except InsufficientFundsError as e:
    print("Custom Error:", e)
```

---

## 🔹 Common Python Exceptions
- `ValueError` → Invalid value type  
- `TypeError` → Wrong type used  
- `ZeroDivisionError` → Divide by zero  
- `FileNotFoundError` → File does not exist  
- `KeyError` → Dictionary key not found  
- `IndexError` → List index out of range  

---

## 🔹 COBOL / Java / C# Mapping
| Concept | COBOL | Java / C# | Python |
|---------|-------|-----------|--------|
| Error Handling | Status codes (`FILE STATUS`) | `try-catch-finally` | `try-except-finally` |
| Raising Errors | Manual RETURN-CODE checks | `throw new Exception()` | `raise Exception()` |
| Custom Errors | Not common | Extend `Exception` class | Subclass `Exception` |

---

## 💡 Exercises
1. Write a program to open a file and handle `FileNotFoundError`.  
2. Write a calculator that handles division by zero gracefully.  
3. Create a custom exception `NegativeValueError` and raise it if user enters a negative number.  
4. Enhance `BankAccount` class: raise `InsufficientFundsError` if withdrawal > balance.  

---
