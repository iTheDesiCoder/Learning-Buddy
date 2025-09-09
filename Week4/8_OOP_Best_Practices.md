# OOP Best Practices in Python

---

## 🔹 Why Best Practices?
- OOP is powerful, but misusing it can make code harder to maintain.  
- Following **best practices** ensures cleaner, reusable, and more efficient code.  

---

## 🔹 1. Use Meaningful Class Names
- Class names should follow **PascalCase**.  
```python
class BankAccount:  
    pass
```

❌ Bad: `class ba:`  
✅ Good: `class BankAccount:`  

---

## 🔹 2. Prefer Composition over Inheritance
- Use **composition** (has-a relationship) instead of always relying on **inheritance** (is-a).  

```python
# Inheritance (can be rigid)
class Engine:
    def start(self):
        print("Engine started")

class Car(Engine):  # Car inherits Engine (not always ideal)
    pass

# Composition (more flexible)
class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

c = Car()
c.start()
```

---

## 🔹 3. Keep Attributes Private (Encapsulation)
- Avoid exposing sensitive attributes directly.  
- Use `@property` and setters.  

```python
class Employee:
    def __init__(self, name, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
```

---

## 🔹 4. Use `__str__` and `__repr__`
- Define human-readable (`__str__`) and developer-readable (`__repr__`) representations.  

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee {self.name}, Salary: {self.salary}"

    def __repr__(self):
        return f"Employee({self.name}, {self.salary})"

e = Employee("Alice", 5000)
print(e)        # Employee Alice, Salary: 5000
print([e])      # [Employee(Alice, 5000)]
```

---

## 🔹 5. Avoid God Classes
- Don’t put **too many responsibilities** in a single class.  
- Follow **Single Responsibility Principle (SRP)**.  

```python
# ❌ Bad: Everything in one class
class Employee:
    def calculate_salary(self): pass
    def save_to_db(self): pass
    def send_email(self): pass

# ✅ Good: Split responsibilities
class Employee: pass
class Payroll: pass
class EmailService: pass
```

---

## 🔹 6. Use Inheritance Carefully
- Don’t overuse inheritance → can create tight coupling.  
- Favor **interfaces/ABCs** for flexibility.  

---

## 🔹 7. Follow Naming Conventions
- Class → `PascalCase`  
- Methods/variables → `snake_case`  
- Constants → `UPPER_CASE`  

---

## 🔹 8. Document Your Classes
- Use **docstrings** to describe purpose and usage.  

```python
class BankAccount:
    """A simple bank account class for managing deposits and withdrawals."""
```

---

## 🔹 COBOL / Java / C# Mapping
| Concept | COBOL | Java / C# | Python |
|---------|-------|-----------|--------|
| Class Design | Procedural only | Strict OOP | Flexible but convention-driven |
| Encapsulation | Not available | Enforced with access modifiers | Convention-based with `_` and `__` |
| Composition vs Inheritance | PERFORMed logic only | Both used | Python recommends composition more |
| Documentation | Comments | Javadoc/XML docs | Docstrings |

---

## 💡 Exercises
1. Create a `BankAccount` class with proper encapsulation, `__str__`, and `__repr__`.  
2. Refactor a class that handles both database and business logic into two separate classes.  
3. Write a class `Library` that uses **composition** (has-a `Book` class). Add methods to borrow and return books.  

---
