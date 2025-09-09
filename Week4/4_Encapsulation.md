# Encapsulation in Python

---

## 🔹 What is Encapsulation?
- **Encapsulation** means bundling **data (attributes)** and **methods (behavior)** into a single unit → the class.  
- It also means **restricting direct access** to some attributes to protect the integrity of the object.  
- In Python, encapsulation is more **convention-based** compared to Java/C#.  

---

## 🔹 Public, Protected, Private in Python

### 1. Public (default)
- Accessible from anywhere.  
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name       # public
        self.salary = salary   # public

emp = Employee("Alice", 6000)
print(emp.name)     # Alice
print(emp.salary)   # 6000
```

### 2. Protected (convention: single underscore `_`)
- Indicates that the attribute should not be accessed directly, but still can be.  
```python
class Employee:
    def __init__(self, name, salary):
        self._salary = salary   # protected

emp = Employee("Bob", 7000)
print(emp._salary)  # 7000 (still accessible, but not recommended)
```

### 3. Private (name mangling with double underscore `__`)
- Python changes the variable name internally to prevent direct access.  
```python
class Employee:
    def __init__(self, name, salary):
        self.__salary = salary   # private

emp = Employee("Charlie", 8000)
# print(emp.__salary)  # ❌ AttributeError
print(emp._Employee__salary)  # ✅ 8000 (name mangling)
```

---

## 🔹 Getter and Setter Methods
- In Python, we often use **methods** to access private attributes.  

```python
class Employee:
    def __init__(self, name, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount

emp = Employee("David", 9000)
print(emp.get_salary())   # 9000
emp.set_salary(9500)
print(emp.get_salary())   # 9500
```

---

## 🔹 Using `@property` for Encapsulation
Python provides a cleaner way with `@property`.  

```python
class Employee:
    def __init__(self, name, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, amount):
        if amount > 0:
            self.__salary = amount

emp = Employee("Eve", 10000)
print(emp.salary)   # calls getter
emp.salary = 11000  # calls setter
print(emp.salary)
```

---

## 🔹 COBOL / Java / C# Mapping
| Concept | COBOL | Java / C# | Python |
|---------|-------|-----------|--------|
| Encapsulation | Not available | Strict `private`, `protected`, `public` | Convention: `_var`, `__var`, `@property` |
| Getter/Setter | PERFORMed logic | Explicit methods (`getSalary()`, `setSalary()`) | `@property` decorator |

---

## 💡 Exercises
1. Create a `BankAccount` class with a private balance attribute. Provide deposit and withdraw methods to update balance safely.  
2. Add `@property` and `@setter` for balance in `BankAccount`. Prevent negative balance assignment.  
3. Create a `Student` class with private marks. Provide a method to update marks only if between 0 and 100.  

---
