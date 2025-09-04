# Python Modules – Basics

---

## 🔹 What is a Module?
- A **module** is simply a Python file (`.py`) that contains code — variables, functions, or classes.  
- Modules help in **organizing** code, avoiding duplication, and promoting **reusability**.  

💡 Example: Instead of writing the same `add` function in multiple programs, we can write it once in a file (`calculator.py`) and reuse it everywhere.

---

## 🔹 Why Use Modules?
- Breaks down large programs into smaller, manageable files.  
- Encourages **code reuse**.  
- Improves **readability** and teamwork.  
- Makes testing and debugging easier.  

👉 **COBOL Mental Mapping**:  
- COBOL uses **COPYBOOKS** (`COPY CUSTOMER-REC.`) to reuse record structures across programs.  
- Python uses **modules** (`import calculator`) to reuse code across files.  

---

## 🔹 Importing Modules

### 1. Import Entire Module
```python
import math
print(math.sqrt(16))  # 4.0
```

### 2. Import With Alias
```python
import math as m
print(m.sqrt(25))  # 5.0
```

### 3. Import Specific Functions
```python
from math import sqrt, pi
print(sqrt(36))  # 6.0
print(pi)        # 3.141592653589793
```

### 4. Import Everything (⚠️ Not Recommended)
```python
from math import *
print(sin(0))
```

💡 Best practice: Import only what you need.  

---

## 🔹 Where Does Python Look for Modules?
- Current directory of the script.  
- Standard library (built-in modules).  
- Third-party installed modules (via `pip`).  

You can check the search path:
```python
import sys
print(sys.path)
```

---

## 🔹 Example

**math_demo.py**
```python
import math

print("Square root of 16 is", math.sqrt(16))
print("Pi value is", math.pi)
```

Run it:  
```bash
python math_demo.py
```

Output:
```
Square root of 16 is 4.0
Pi value is 3.141592653589793
```

---

## 💡 Exercises

1. Write a Python program that uses the `math` module to calculate factorial of 5.  
2. Import the `datetime` module and print today’s date.  
3. Use `from math import pi` and display the area of a circle with radius 7.  
4. Print the module search path using `sys.path`.  

---
