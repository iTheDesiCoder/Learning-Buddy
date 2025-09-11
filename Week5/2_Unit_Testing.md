# Unit Testing in Python

---

## 🔹 What is Unit Testing?
- **Unit testing** is the process of testing small parts of your program (functions, methods, classes).  
- Ensures that each piece works correctly **in isolation**.  
- Helps prevent bugs when making changes.  

---

## 🔹 Why Unit Testing?
- Early bug detection.  
- Makes refactoring safe.  
- Improves code reliability.  
- Encourages modular design.  

---

## 🔹 Using `assert` for Simple Testing
```python
def add(a, b):
    return a + b

# Simple test
assert add(2, 3) == 5
assert add(-1, 1) == 0
print("All tests passed!")
```

---

## 🔹 The `unittest` Module
Python’s built-in testing framework.

```python
import unittest

def multiply(a, b):
    return a * b

class TestMath(unittest.TestCase):
    def test_multiply_positive(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-1, 5), -5)

if __name__ == "__main__":
    unittest.main()
```

Run:
```bash
python test_math.py
```

---

## 🔹 Common Assertions in `unittest`
- `assertEqual(a, b)` → a == b  
- `assertNotEqual(a, b)` → a != b  
- `assertTrue(x)` → x is True  
- `assertFalse(x)` → x is False  
- `assertIn(a, b)` → a in b  
- `assertRaises(Error)` → checks if exception is raised  

---

## 🔹 Example: Testing BankAccount
```python
import unittest

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        acc = BankAccount(100)
        acc.deposit(50)
        self.assertEqual(acc.balance, 150)

    def test_withdraw(self):
        acc = BankAccount(200)
        acc.withdraw(100)
        self.assertEqual(acc.balance, 100)

    def test_withdraw_insufficient(self):
        acc = BankAccount(50)
        with self.assertRaises(ValueError):
            acc.withdraw(100)

if __name__ == "__main__":
    unittest.main()
```

---

## 🔹 Pytest (Optional – Popular Framework)
Install:
```bash
pip install pytest
```

Example:
```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

Run:
```bash
pytest test_sample.py
```

---

## 🔹 COBOL / Java / C# Mapping
| Concept | COBOL | Java / C# | Python |
|---------|-------|-----------|--------|
| Unit Testing | Manual, test jobs | JUnit, NUnit, MSTest | `unittest`, `pytest` |
| Assertions | DISPLAY + compare manually | `assertEquals`, `assertTrue` | `assertEqual`, `assertTrue` |
| Test Runner | Manual batch job | IDE or command-line tools | CLI: `python -m unittest`, `pytest` |

---

## 💡 Exercises
1. Write a function `is_even(n)` and test it with unittest.  
2. Add a `transfer` method in `BankAccount` and write tests for it.  
3. Write a custom exception `OverdraftError` and test that it is raised correctly.  
4. Try the same tests using `pytest`.  

---
