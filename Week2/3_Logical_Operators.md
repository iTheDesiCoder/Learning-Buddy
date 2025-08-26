# Python Basics – Operators

---

## 🔹 Arithmetic Operators

### Examples
```python
a, b = 10, 3
print("Addition:", a + b)     # 13
print("Subtraction:", a - b)  # 7
print("Multiplication:", a * b) # 30
print("Division:", a / b)     # 3.333...
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)      # 1
print("Power:", a ** b)       # 1000
```

### How It Is Different
- **COBOL**: Uses `ADD`, `SUBTRACT`, `MULTIPLY`, `DIVIDE` verbs.  
- **C/Java/C#**: Same symbols for operators, but division differs (integer division vs float).  
- **Python**: `/` always returns float, `//` is floor division.  

### 💡 Exercise
Write a program to calculate area of a circle given radius `r`.  

---

## 🔹 Relational (Comparison) Operators

### Examples
```python
x, y = 5, 10
print(x == y)   # False
print(x != y)   # True
print(x > y)    # False
print(x < y)    # True
print(x >= 5)   # True
print(y <= 10)  # True
```

### How It Is Different
- **COBOL**: Uses `IF A = B` or `IF A GREATER THAN B`.  
- **C/Java/C#**: Similar relational operators.  
- **Python**: Supports **chained comparisons**.  

```python
x = 7
print(5 < x < 10)   # True
```

### 💡 Exercise
Check if a number lies between 100 and 200 (inclusive).  

---

## 🔹 Logical Operators

### Examples
```python
is_raining = False
has_umbrella = True

print(is_raining and has_umbrella)  # False
print(is_raining or has_umbrella)   # True
print(not is_raining)               # True
```

### How It Is Different
- **COBOL**: Uses `AND`, `OR`, `NOT` keywords.  
- **C/Java/C#**: Uses `&&`, `||`, `!`.  
- **Python**: Uses plain English words `and`, `or`, `not`.  

### 💡 Exercise
Write a program to check if a year is a leap year:  
- Divisible by 4, but not by 100, unless divisible by 400.  

---

## 🔹 Identity and Membership Operators

### Identity (`is`, `is not`)
```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)      # True (same object)
print(x is z)      # False (different objects with same content)
```

### Membership (`in`, `not in`)
```python
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)     # True
print("grape" not in fruits) # True
```

### 💡 Exercise
- Use `is` to show difference between two variables pointing to same list vs two identical lists.  
- Use `in` to check if "python" exists in the string `"I am learning python"`.  

---
