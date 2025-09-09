# Inheritance in Python

---

## 🔹 What is Inheritance?
- **Inheritance** allows a class (child) to reuse code from another class (parent).  
- Helps with **code reusability** and **hierarchy modeling**.  
- Example: `SavingsAccount` inherits from `BankAccount`.  

---

## 🔹 Basic Inheritance

```python
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.05):
        super().__init__(account_number, balance)  # call parent constructor
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

acc = SavingsAccount("S1001", 1000)
acc.deposit(500)
acc.add_interest()
print(acc.balance)  # 1575.0
```

---

## 🔹 Types of Inheritance in Python

1. **Single Inheritance** → One parent, one child.  
```python
class Parent:
    pass
class Child(Parent):
    pass
```

2. **Multiple Inheritance** → Child inherits from multiple parents.  
```python
class A:
    def method_a(self):
        print("A")

class B:
    def method_b(self):
        print("B")

class C(A, B):
    pass

c = C()
c.method_a()  # A
c.method_b()  # B
```

3. **Multilevel Inheritance** → Parent → Child → Grandchild.  
```python
class Grandparent:
    pass
class Parent(Grandparent):
    pass
class Child(Parent):
    pass
```

4. **Hierarchical Inheritance** → One parent, multiple children.  
```python
class Parent:
    pass
class Child1(Parent):
    pass
class Child2(Parent):
    pass
```

5. **Hybrid Inheritance** → Combination of the above.  

---

## 🔹 Method Overriding
Child class can redefine parent methods.

```python
class BankAccount:
    def deposit(self, amount):
        print(f"Depositing {amount} to account")

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        print(f"Depositing {amount} with extra logging")

acc = SavingsAccount()
acc.deposit(500)
```

---

## 🔹 The `super()` Function
- Used to call parent class methods/constructors.  
- Avoids repeating code.  

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

c = Child("Alice", 20)
print(c.name, c.age)
```

---

## 🔹 MRO (Method Resolution Order)
- Python uses **C3 linearization** to resolve methods in multiple inheritance.  
- Check order with:
```python
print(C.__mro__)
```

---

## 🔹 COBOL / Java / C# Mapping
| Concept | COBOL | Java / C# | Python |
|---------|-------|-----------|--------|
| Inheritance | Not available | `extends`, `:` | `class Child(Parent):` |
| Multiple Inheritance | Not available | Not supported in Java (only interfaces) | Supported |
| Method Overriding | PERFORM new logic | `@Override` | Redefine method in child |
| super() | Not available | `super()` | `super()` |

---

## 💡 Exercises
1. Create a `Vehicle` class with a method `start()`. Create a `Car` class that inherits `Vehicle` and overrides `start()`.  
2. Create a `Person` class with attributes `name` and `age`. Create a `Student` class that inherits `Person` and adds `grade`.  
3. Implement multiple inheritance with `Teacher` and `Researcher` classes, then create a `Professor` class that inherits from both.  

---
