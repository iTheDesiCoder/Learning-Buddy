# Creating Your Own Module in Python

---

## 🔹 What is a Module?
- A **module** is just a Python file (`.py`) containing code (functions, variables, or classes).  
- You can create your own modules to **organize** and **reuse** code across multiple programs.  

👉 **COBOL Mental Mapping**:  
- COBOL developers use **COPYBOOKS** to share record layouts across programs.  
- In Python, we use **custom modules** to share functions and logic.

---

## 🔹 Steps to Create and Use a Module

### 1. Create a Module File

**calculator.py**
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
```

---

### 2. Import the Module in Another File

**main.py**
```python
import calculator

print("Add:", calculator.add(10, 5))       # 15
print("Subtract:", calculator.subtract(10, 5)) # 5
print("Multiply:", calculator.multiply(10, 5)) # 50
print("Divide:", calculator.divide(10, 5))     # 2.0
```

Run the program:  
```bash
python main.py
```

---

### 3. Import Specific Functions
```python
from calculator import add, divide

print(add(7, 3))    # 10
print(divide(10, 2)) # 5.0
```

---

### 4. Import With Alias
```python
import calculator as calc

print(calc.multiply(4, 5))  # 20
```

---

## 🔹 Module Search Path
When you `import` a module, Python looks in:  
1. Current directory of the script.  
2. Standard library folders.  
3. Third-party packages (installed via pip).  

You can check the search path:
```python
import sys
print(sys.path)
```

If your module is not in the same folder, you can adjust `sys.path` or use packages.  

---

## 🔹 Real-World Example

### File: `greetings.py`
```python
def hello(name):
    return f"Hello, {name}!"

def goodbye(name):
    return f"Goodbye, {name}!"
```

### File: `main.py`
```python
import greetings

print(greetings.hello("Alice"))
print(greetings.goodbye("Alice"))
```

Output:
```
Hello, Alice!
Goodbye, Alice!
```

---

## 💡 Exercises

1. Create a module `mathutils.py` with functions: `square(n)`, `cube(n)`.  
   Import and use them in another file.  
2. Write a module `strings.py` with a function `reverse(s)` that reverses a string.  
3. Create a module `finance.py` with a function `simple_interest(p, r, t)` and test it.  
4. Print the module search path using `sys.path`.  

---
