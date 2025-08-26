# Python Basics – Control Structures

---

## 🔹 Conditional Statements (if, elif, else)

### 1. How to Define
```python
age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### 2. With `elif`
```python
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
```

### 3. How It Is Different
- **COBOL**: Uses `IF ... ELSE` but with verbose syntax.  
- **C/Java/C#**: Very similar `if-else` structure.  
- **Python**: Uses **indentation instead of braces**.  

### 💡 Exercise
Write a program to check:  
- If a number is positive, print `"Positive"`  
- If it is zero, print `"Zero"`  
- Otherwise, print `"Negative"`  

---

## 🔹 Loops – For Loop

### 1. How to Define
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### 2. With Range
```python
for i in range(1, 6):
    print(i)
```

### 3. How It Is Different
- **COBOL**: Loops with `PERFORM UNTIL`.  
- **C/Java/C#**: Use `for(init; condition; increment)` or enhanced for-each.  
- **Python**: Iterates **directly over sequences** (lists, strings, ranges).  

### 💡 Exercise
Write a loop to print numbers from 1 to 20.  
Modify it to print only even numbers.  

---

## 🔹 Loops – While Loop

### 1. How to Define
```python
count = 3
while count > 0:
    print("Countdown:", count)
    count -= 1
```

### 2. How It Is Different
- **COBOL**: Uses `PERFORM UNTIL` or `PERFORM VARYING`.  
- **C/Java/C#**: Same concept of `while(condition) { ... }`.  
- **Python**: Condition-based loop, ends when false.  

### 💡 Exercise
Write a while loop to calculate the sum of numbers from 1 to 100.  

---

## 🔹 Loop Control Statements

### Break
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### Continue
```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

### Else with Loop
```python
for i in range(5):
    print(i)
else:
    print("Loop finished normally")
```

### How It Is Different
- **COBOL**: Does not have `break` or `continue`.  
- **C/Java/C#**: Has `break` and `continue`, but not `else` with loops.  
- **Python**: Unique `else` clause executes if loop finishes without `break`.  

### 💡 Exercise
Write a loop to check if a number is prime.  
Use `break` if a divisor is found, otherwise `else` prints `"Prime"`.  

---
