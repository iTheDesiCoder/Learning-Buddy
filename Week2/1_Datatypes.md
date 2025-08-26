# Python Basics – Data Types

---

## 🔹 Integers (`int`)

### 1. How to Define
```python
x = 10
y = -5
z = int("42")   # from string
```

### 2. How It Is Different
- **COBOL**: Fixed-size numeric storage (`PIC 9(4)` = exactly 4 digits).  
- **C/Java/C#**: Multiple integer types (`int`, `long`, `short`) with fixed size (32-bit, 64-bit).  
- **Python**: Only **one `int` type**, automatically grows in size.  

### 3. Any Limit?
```python
big = 999999999999999999999999999999
print(big)  # works fine, no overflow
```
- No overflow (limited only by memory).  
- Slower than C/Java for huge numbers.  

### 4. How It Works (`id()` demo)
```python
a = 10
b = 10
print(id(a), id(b))   # same id → small ints (-5 to 256) are reused

c = 1000
d = 1000
print(id(c), id(d))   # may differ → large ints not cached
```

💡 **Takeaway**: Integers are **immutable objects** → operations create new objects.

---

## 🔹 Floats (`float`)

### 1. How to Define
```python
pi = 3.14
neg = -0.5
f = float("2.718")
```

### 2. How It Is Different
- **COBOL**: Fixed-point arithmetic (`COMP-3` for decimals).  
- **C/Java/C#**: `float` (32-bit), `double` (64-bit).  
- **Python**: `float` = double precision (64-bit IEEE 754).  

### 3. Any Limit?
- Large/small values possible, but not infinite precision.  
```python
print(0.1 + 0.2)   # 0.30000000000000004
```

### 4. How It Works
- Stored as 64-bit binary floating point.  
- Subject to rounding errors.

---

## 🔹 Strings (`str`)

### 1. How to Define
```python
s1 = "Hello"
s2 = 'World'
s3 = """Multi
line
string"""
```

### 2. How It Is Different
- **COBOL**: Fixed-length fields (`PIC X(20)`), padded with spaces.  
- **C#/Java**: Strings are immutable objects.  
- **Python**: Also immutable → every modification creates a new string.  

### 3. Any Limit?
- No fixed size (limited by memory).  

### 4. How It Works (`id()` demo)
```python
s = "hello"
print(id(s))

s = s.upper()   # creates a NEW string
print(id(s))    # different id
```

💡 **Takeaway**: Strings are **immutable**.  

---

## 🔹 Lists (`list`)

### 1. How to Define
```python
fruits = ["apple", "banana", "cherry"]
```

### 2. How It Is Different
- **COBOL**: Tables are fixed-size.  
- **C/Java/C#**: Arrays have fixed size; use `ArrayList`/`List<T>` for dynamic.  
- **Python**: Built-in dynamic list, can grow/shrink, and hold mixed types.  

### 3. Any Limit?
- No fixed size → expands dynamically.  

### 4. How It Works (`id()` demo)
```python
lst1 = [1, 2, 3]
lst2 = lst1
lst1.append(4)

print(lst1, lst2)           # [1, 2, 3, 4] [1, 2, 3, 4]
print(id(lst1), id(lst2))   # same id → same object
```

💡 **Takeaway**: Lists are **mutable**.  

---

## 🔹 Tuple (`tuple`)

### 1. How to Define
```python
point = (10, 20)
```

### 2. How It Is Different
- **Python**: Like a list but immutable.  
- Useful for fixed collections (coordinates, configs).  

### 3. Any Limit?
- Same as list, but contents cannot be changed.  

### 4. How It Works
```python
t = (1, 2, 3)
# t[0] = 99   # ❌ TypeError
```

💡 **Takeaway**: Tuples are **immutable lists**.  

---

## 🔹 Dictionary (`dict`)

### 1. How to Define
```python
person = {"name": "Alice", "age": 30}
```

### 2. How It Is Different
- **COBOL**: Lookup tables via `OCCURS ... INDEXED BY`.  
- **C#/Java**: `Dictionary<K,V>` / `HashMap<K,V>`.  
- **Python**: Built-in, very fast for lookups.  

### 3. Any Limit?
- Keys must be immutable.  
- Values can be anything.  

### 4. How It Works
```python
person["age"] = 31   # update
print(person)        # {'name': 'Alice', 'age': 31}
```

💡 **Takeaway**: Dicts are **mutable key-value stores**.  

---

## 🔹 Set (`set`)

### 1. How to Define
```python
nums = {1, 2, 3, 3}
print(nums)   # {1, 2, 3}
```

### 2. How It Is Different
- **Java/C#**: Need `HashSet` class.  
- **Python**: Built-in, like mathematical sets.  

### 3. Any Limit?
- No duplicates.  
- Elements must be immutable.  

### 4. How It Works
```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))        # {1, 2, 3, 4, 5}
print(a.intersection(b)) # {3}
```

💡 **Takeaway**: Sets are **mutable**, unordered, unique collections.  

---

## 🔹 Boolean (`bool`) and `None`

### Boolean
```python
flag = True
print(flag, type(flag))  # True <class 'bool'>
```

### None (like null)
```python
value = None
print(value is None)     # True
```

---
