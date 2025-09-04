# Python Third-Party Modules

---

## 🔹 What are Third-Party Modules?
- Python allows you to extend functionality using **external libraries** created by the community.  
- These are hosted on **PyPI (Python Package Index)**.  
- You install them using **pip** (Python’s package manager).  

👉 **COBOL/Java/C# Mapping**:  
- COBOL: Vendor-supplied libraries linked at compile/run time.  
- Java: Maven/Gradle dependencies (JARs).  
- C#: NuGet packages (DLLs).  
- Python: PyPI packages installed via `pip`.  

---

## 🔹 Installing Third-Party Modules

Check pip version:
```bash
pip --version
```

Install a package:
```bash
pip install requests
```

Upgrade a package:
```bash
pip install --upgrade requests
```

Uninstall a package:
```bash
pip uninstall requests
```

List installed packages:
```bash
pip list
```

---

## 🔹 Example 1: `requests` (HTTP Requests)
```python
import requests

response = requests.get("https://api.github.com")
print("Status:", response.status_code)
print("Content type:", response.headers["content-type"])
print("Body:", response.json())
```

---

## 🔹 Example 2: `pandas` (Data Analysis)
```python
import pandas as pd

data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)
print(df)
```

Output:
```
    Name  Age
0  Alice   25
1    Bob   30
```

---

## 🔹 Example 3: `numpy` (Numerical Computing)
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Square Roots:", np.sqrt(arr))
```

---

## 🔹 Virtual Environments
- Helps isolate dependencies for each project.  
- Prevents conflicts between package versions.  

Create venv:
```bash
python -m venv myenv
```

Activate venv (Windows):
```bash
myenv\Scripts\activate
```

Activate venv (Linux/Mac):
```bash
source myenv/bin/activate
```

Deactivate venv:
```bash
deactivate
```

---

## 🔹 Real-World Use Cases
- `requests` → API calls, web scraping.  
- `pandas` → Finance data analysis.  
- `numpy` → Scientific computing, ML.  
- `sqlalchemy` → Database access.  
- `flask` / `django` → Web frameworks.  

---

## 💡 Exercises

1. Install the `requests` library and fetch data from `https://api.github.com`.  
2. Install `pandas` and create a DataFrame for employee salaries.  
3. Use `numpy` to calculate the mean and standard deviation of a list of numbers.  
4. Create and activate a virtual environment, then install `flask` inside it.  

---
