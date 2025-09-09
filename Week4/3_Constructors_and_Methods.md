# Constructors and Methods in Python

---

## 🔹 What is a Constructor?
- A **constructor** is a special method used to initialize objects.  
- In Python, the constructor is defined using **`__init__`**.  
- It runs **automatically** when an object is created.  

Example:
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp = Employee("Alice", 6000)
print(emp.name, emp.salary)  # Alice 6000
```

---

## 🔹 Instance Methods
- Methods that operate on **individual objects**.  
- Must include `self` as the first parameter (represents the object).  

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee {self.name}, Salary: {self.salary}")

emp = Employee("Bob", 7000)
emp.display()  # Employee Bob, Salary: 7000
```

---

## 🔹 Class Variables vs Instance Variables

- **Instance Variables** → unique to each object.  
- **Class Variables** → shared across all objects.  

```python
class Employee:
    company_name = "TechCorp"  # class variable

    def __init__(self, name, salary):
        self.name = name       # instance variable
        self.salary = salary   # instance variable

emp1 = Employee("Alice", 6000)
emp2 = Employee("Bob", 7000)

print(emp1.company_name)  # TechCorp
print(emp2.company_name)  # TechCorp
```

---

## 🔹 Class Methods
- Defined using `@classmethod`.  
- Operate on the **class itself**, not individual objects.  
- First parameter is `cls` (refers to the class).  

```python
class Employee:
    company_name = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

emp1 = Employee("Alice", 6000)
emp2 = Employee("Bob", 7000)

Employee.change_company("NewTech")
print(emp1.company_name)  # NewTech
print(emp2.company_name)  # NewTech
```

---

## 🔹 Static Methods
- Defined using `@staticmethod`.  
- Don’t use `self` or `cls`.  
- Used for **utility functions** that don’t depend on object or class.  

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 10))  # 15
```

---

## 🔹 COBOL / Java / C# Mapping
| Concept | COBOL | Java / C# | Python |
|---------|-------|-----------|--------|
| Constructor | Not applicable | `public Employee(...) {}` | `def __init__(...)` |
| Instance Method | PERFORM sections | Methods inside classes | Defined with `self` |
| Class Variable | WORKING-STORAGE (global) | `static` keyword | Defined outside `__init__` |
| Class Method | Not available | `static` methods with `class` access | `@classmethod` |
| Static Method | Not available | `static` keyword | `@staticmethod` |

---

## 💡 Exercises
1. Create a `Car` class with a class variable `wheels = 4`. Add an instance variable for `brand`. Write a method to display details.  
2. Create an `Employee` class with a static method `is_valid_salary(salary)` that returns `True` if salary > 0.  
3. Add a class method `set_company(name)` to `Employee` that changes the company name for all employees.  

---
