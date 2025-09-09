# Abstraction in Python

---

## 🔹 What is Abstraction?
- **Abstraction** means hiding the internal implementation and exposing only the necessary details.  
- Helps reduce complexity by focusing on **what** an object does rather than **how** it does it.  

👉 Example: When you use a `car.start()`, you don’t worry about how the engine works internally.  

---

## 🔹 Abstraction in Python
- Python does not enforce abstraction like Java/C#.  
- But it provides tools to achieve it:  
  1. **Abstract Base Classes (ABC module)**  
  2. **Interfaces (via abstract methods)**  

---

## 🔹 Abstract Base Classes
- Use the `abc` module (`ABC`, `abstractmethod`).  
- A class with abstract methods **cannot be instantiated**.  
- Child classes must implement abstract methods.  

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c = Circle(5)
print(c.area())  # 78.5
```

---

## 🔹 Interfaces in Python
- Python doesn’t have `interface` keyword like Java.  
- Instead, abstract base classes serve the same purpose.  

```python
from abc import ABC, abstractmethod

class Playable(ABC):
    @abstractmethod
    def play(self):
        pass

class Guitar(Playable):
    def play(self):
        print("Strumming the guitar")

class Piano(Playable):
    def play(self):
        print("Playing the piano")

for instrument in [Guitar(), Piano()]:
    instrument.play()
```

---

## 🔹 Partial Abstraction
- A class can have both **abstract** and **concrete** methods.  

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Vehicle stopped")

class Car(Vehicle):
    def start(self):
        print("Car started")

c = Car()
c.start()
c.stop()
```

---

## 🔹 COBOL / Java / C# Mapping
| Concept | COBOL | Java / C# | Python |
|---------|-------|-----------|--------|
| Abstraction | Not available | `abstract` classes, `interface` keyword | `abc` module (`ABC`, `abstractmethod`) |
| Interfaces | Not available | `interface` keyword | Achieved using ABCs |
| Partial Abstraction | Not available | Abstract + concrete methods | Supported |

---

## 💡 Exercises
1. Create an abstract class `Employee` with an abstract method `calculate_pay()`. Implement it in `FullTimeEmployee` and `ContractEmployee`.  
2. Create an abstract class `Appliance` with abstract method `operate()`. Implement `WashingMachine` and `Microwave`.  
3. Extend `Vehicle` class to include `Bus` and `Bike` classes with their own `start()` methods.  

---
