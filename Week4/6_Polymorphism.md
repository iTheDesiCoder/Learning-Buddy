# Polymorphism in Python

---

## 🔹 What is Polymorphism?
- **Polymorphism** means "many forms".  
- In OOP, it allows the same method or operator to behave differently based on the object.  
- Helps write **flexible and reusable code**.  

---

## 🔹 Method Overriding (Run-time Polymorphism)
- A child class provides a specific implementation of a method already defined in its parent.  

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

animals = [Dog(), Cat()]
for a in animals:
    a.speak()
# Woof!
# Meow!
```

---

## 🔹 Duck Typing in Python
- Python cares about **behavior, not type**.  
- If an object has the required method, it can be used, regardless of its class.  

```python
class Duck:
    def sound(self):
        print("Quack!")

class Person:
    def sound(self):
        print("Hello!")

def make_sound(obj):
    obj.sound()

make_sound(Duck())    # Quack!
make_sound(Person())  # Hello!
```

---

## 🔹 Operator Overloading
- Polymorphism also applies to operators.  
- In Python, operators are implemented using special methods like `__add__`, `__sub__`.  

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)  # (6, 8)
```

---

## 🔹 Built-in Polymorphism
Many built-in functions support polymorphism.  

```python
print(len("Python"))     # 6 (string)
print(len([10, 20, 30])) # 3 (list)
```

---

## 🔹 COBOL / Java / C# Mapping
| Concept | COBOL | Java / C# | Python |
|---------|-------|-----------|--------|
| Polymorphism | Not available | Method overriding & interfaces | Method overriding, duck typing |
| Operator Overloading | Not available | Limited (C# supports `operator+`) | Fully supported with `__add__`, etc. |
| Duck Typing | Not available | Not supported (strong typing) | Fully supported |

---

## 💡 Exercises
1. Create a base class `Shape` with a method `area()`. Override it in `Circle` and `Rectangle`.  
2. Implement operator overloading for a `Time` class so that adding two times returns a new time.  
3. Write a function `play(obj)` that accepts any object with a `play()` method (duck typing). Test it with a `Guitar` and `Piano` class.  

---
