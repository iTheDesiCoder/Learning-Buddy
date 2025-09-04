# Python Built-In Modules

---

## 🔹 What are Built-in Modules?
- Python comes with a **Standard Library** often called **"Batteries Included"**.  
- These are modules you can use **without installing anything**.  
- They cover areas like math, file handling, date/time, data serialization, system operations, and more.  

👉 **COBOL Mental Mapping**:  
- In COBOL, many operations (like string handling, arithmetic, file IO) are built into the language.  
- In Python, instead of writing everything yourself, you **import** from the standard library.  

---

## 🔹 Common Built-in Modules

### 1. `math` – Mathematical Functions
```python
import math

print(math.sqrt(25))    # 5.0
print(math.factorial(5)) # 120
print(math.pi)          # 3.141592653589793
```

---

### 2. `datetime` – Date and Time
```python
import datetime

today = datetime.date.today()
print("Today's date:", today)

now = datetime.datetime.now()
print("Current time:", now)
```

---

### 3. `os` – Operating System Interface
```python
import os

print("Current Working Directory:", os.getcwd())
print("List of files:", os.listdir("."))
```

---

### 4. `sys` – Python Interpreter Details
```python
import sys

print("Python version:", sys.version)
print("Module search path:", sys.path)
```

---

### 5. `json` – Working with JSON Data
```python
import json

data = '{"name": "Alice", "age": 30}'
parsed = json.loads(data)
print(parsed["name"])  # Alice

person = {"name": "Bob", "age": 25}
json_str = json.dumps(person)
print(json_str)  # {"name": "Bob", "age": 25}
```

---

## 🔹 How to Explore Modules
- List all available modules:
```python
help("modules")
```

- Get help on a specific module:
```python
help("math")
```

- List all functions inside a module:
```python
import math
print(dir(math))
```

---

## 🔹 Example Program

**std_demo.py**
```python
import math, datetime, os

print("Pi:", math.pi)
print("Factorial of 6:", math.factorial(6))
print("Today:", datetime.date.today())
print("Files in current directory:", os.listdir("."))
```

---

## 💡 Exercises

1. Use the `math` module to calculate the square root of 144.  
2. Print today’s date and current time using the `datetime` module.  
3. Display the Python version using the `sys` module.  
4. Convert a Python dictionary into JSON using the `json` module.  
5. Use `os.listdir()` to list files in the current directory.  

---
