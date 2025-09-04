# Python Modules – Best Practices

---

## 🔹 Why Best Practices Matter?
- Helps keep projects **organized** and **maintainable**.  
- Avoids common pitfalls like circular imports or poor naming.  
- Makes teamwork and code reuse easier.  

---

## 🔹 1. Naming Conventions
- Use **lowercase names** for module files.  
- Use underscores `_` for readability if needed.  
- Example: `mathutils.py`, `string_utils.py`.  

❌ Bad: `MyModule.PY`  
✅ Good: `finance_tools.py`  

---

## 🔹 2. Organizing Code
- Group related functions in the same module.  
- Split large projects into **packages**.  
- Keep modules focused on **one responsibility**.  

Example project layout:
```
project/
    __init__.py
    mathutils.py
    stringutils.py
    finance/
        __init__.py
        interest.py
        tax.py
```

---

## 🔹 3. Avoid Circular Imports
Circular imports happen when two modules import each other.  

❌ Example:
```python
# a.py
import b

# b.py
import a
```

This leads to `ImportError`.  

✅ Solution:  
- Restructure code.  
- Move shared functions into a separate helper module.  

---

## 🔹 4. Use `if __name__ == "__main__":`
- Allows modules to run standalone for testing.  
- Prevents unwanted execution when imported.  

Example:
```python
def greet(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    print(greet("Alice"))
```

---

## 🔹 5. Virtual Environments
- Always use **virtual environments** to isolate project dependencies.  
- Prevents conflicts between packages.  

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

## 🔹 6. Document Your Modules
- Add docstrings to functions and modules.  
- Makes it easier for others to understand and reuse.  

Example:
```python
"""
mathutils.py - Utility functions for math operations
"""

def square(n):
    """Returns square of n"""
    return n * n
```

---

## 🔹 7. Consistent Imports
- Prefer **explicit imports** over `from module import *`.  
- Keeps code clear about where functions come from.  

❌ Bad:
```python
from math import *
print(sqrt(16))
```

✅ Good:
```python
from math import sqrt
print(sqrt(16))
```

---

## 🔹 8. Dependency Management
- Use `requirements.txt` to track dependencies.  
- Example:
```
requests==2.31.0
pandas==2.1.1
numpy==1.26.0
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🔹 COBOL / Java / C# Mapping
- COBOL: Strict program structure, COPYBOOK reuse → Python needs discipline via packages.  
- Java: Enforced package structure → Python flexible, but convention-driven.  
- C#: Namespaces/Assemblies enforce modularity → Python relies on folder/package discipline.  

---

## 💡 Exercises

1. Create a new project folder with two modules (`mathutils.py`, `stringutils.py`) and a main program.  
2. Add proper docstrings to each function.  
3. Run a module directly and confirm `if __name__ == "__main__":` works.  
4. Write a `requirements.txt` with two third-party packages and install them in a virtual environment.  

---
