# Python Packages and `__init__.py`

---

## 🔹 What is a Package?
- A **module** is a single Python file (`.py`).  
- A **package** is a collection of modules organized in a folder.  
- To make Python treat a folder as a package, it must contain a special file: **`__init__.py`**.  

👉 **COBOL Mental Mapping**:  
- COBOL uses **COPYBOOKS** for reusable record layouts.  
- A **package** in Python is like a **library of COPYBOOKS** bundled together.

---

## 🔹 Why Use Packages?
- Organize large projects into smaller parts.  
- Avoid module name conflicts.  
- Promote code reuse across teams.  

---

## 🔹 `__init__.py` File
- Marks a directory as a **Python package**.  
- Can be empty (just indicates "this is a package").  
- Can also execute initialization code (define variables, import submodules).  

Example `mypackage/__init__.py`:
```python
print("Initializing mypackage")
PI = 3.14159
```

When you import the package, this code runs.  

---

## 🔹 Creating a Package

### Project Structure
```
mypackage/
    __init__.py
    mathutils.py
    stringutils.py
```

### File: `mypackage/mathutils.py`
```python
def square(n):
    return n * n

def cube(n):
    return n * n * n
```

### File: `mypackage/stringutils.py`
```python
def reverse(s):
    return s[::-1]

def capitalize_words(s):
    return s.title()
```

### File: `main.py`
```python
import mypackage.mathutils as mu
import mypackage.stringutils as su

print(mu.square(4))         # 16
print(su.capitalize_words("hello cobol world"))  # Hello Cobol World
```

---

## 🔹 Importing from Packages

### Import Entire Module
```python
import mypackage.mathutils
print(mypackage.mathutils.square(5))  # 25
```

### Import Specific Functions
```python
from mypackage.mathutils import cube
print(cube(3))  # 27
```

### Import with Alias
```python
import mypackage.stringutils as su
print(su.reverse("python"))  # nohtyp
```

---

## 🔹 Using `__init__.py` for Shortcuts
You can re-export functions so users don’t need to go deep into submodules.

**mypackage/__init__.py**
```python
from .mathutils import square, cube
from .stringutils import reverse
```

Now you can do:
```python
from mypackage import square, reverse

print(square(6))    # 36
print(reverse("abc")) # cba
```

---

## 🔹 Real-World Example
- **Django** is a package with many submodules (`django.http`, `django.urls`, etc.).  
- **NumPy** is a package with hundreds of mathematical submodules.  

---

## 💡 Exercises

1. Create a package `finance/` with modules:  
   - `interest.py` → function `simple_interest(p, r, t)`  
   - `tax.py` → function `calculate_tax(income)`  
   Import and test them in `main.py`.  

2. Add an `__init__.py` file to `finance/` that re-exports both functions.  
   Test them with:  
   ```python
   from finance import simple_interest, calculate_tax
   ```

3. Modify `__init__.py` to print `"Finance package initialized"` when imported.  

---
