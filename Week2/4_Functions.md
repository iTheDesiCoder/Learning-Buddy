# Python Basics – Functions

---

## 🔹 What is a Function?
- A reusable block of code that performs a specific task.  
- Helps avoid repetition, makes code modular and organized.  

---

## 🔹 Defining a Function

### Basic Function
```python
def greet():
    print("Hello, welcome to Python!")

greet()   # calling the function
```

### With Parameters
```python
def add(a, b):
    return a + b

print(add(5, 7))  # 12
```

### With Default Parameters
```python
def power(base, exp=2):
    return base ** exp

print(power(5))    # 25 (default exp=2)
print(power(5, 3)) # 125
```

---

## 🔹 How Functions Differ (COBOL, Java, C#)

- **COBOL**: Uses `PERFORM` for procedures, does not return values in the same way.  
- **Java/C#**: Must declare return type (`int add(int a, int b)`).  
- **Python**: No type declaration needed, return type is flexible.  

```python
def demo():
    return "Hello", 42

print(demo())   # ('Hello', 42)
```

---

## 🔹 Variable Scope

```python
x = 10   # global

def my_func():
    x = 5  # local
    print("Inside:", x)

my_func()
print("Outside:", x)
```

💡 Variables inside a function are **local** unless declared `global`.  

---

## 🔹 Lambda (Anonymous Functions)

```python
square = lambda n: n * n
print(square(5))  # 25

# useful in higher-order functions
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, nums))
print(squares)  # [1, 4, 9, 16, 25]
```

---

## 🔹 Docstrings

```python
def multiply(a, b):
    """This function multiplies two numbers."""
    return a * b

print(multiply.__doc__)
```

---

## 💡 Exercises

1. Write a function `is_even(n)` that returns `True` if `n` is even, else `False`.  
2. Write a function `factorial(n)` that calculates factorial using a loop.  
3. Write a function `greet_user(name, age)` that prints:  
   `"Hello Alice, you are 30 years old."`  
4. Convert a list of Celsius temperatures into Fahrenheit using `map()` and a `lambda`.  

---
