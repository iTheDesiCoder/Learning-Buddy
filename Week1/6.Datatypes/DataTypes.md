# Data Types in Python (Mutable vs Immutable)

---

## 🔹 Basic Types
- `int`, `float` → numbers
- `str` → text
- `bool` → `True` / `False`
- `None` → null-like value

---

## 🔹 Collection Types
- `list` → ordered, **mutable**
- `tuple` → ordered, **immutable**
- `set` → unordered, unique elements, **mutable**
- `dict` → key-value pairs, **mutable**

---

## 🔹 Immutable Examples
```python
x = 10
y = x
x = x + 1

print(x)  # 11
print(y)  # 10 (unchanged)

s = "hello"
# s[0] = "H"   # ❌ TypeError
s = "Hello"    # ✅ creates a new string
```

## 🔹 Mutable Examples
```python
lst1 = [1, 2, 3]
lst2 = lst1     # both point to same list
lst1[0] = 99

print(lst1)  # [99, 2, 3]
print(lst2)  # [99, 2, 3] → changed too!
```