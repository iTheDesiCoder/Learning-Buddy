# 🧮 NumPy Tutorial

## 1. Introduction
- **NumPy** stands for **Numerical Python**.
- It provides support for large, multi-dimensional arrays and matrices.
- Offers mathematical functions to operate on arrays efficiently.
- Compared to Python lists:
  - Faster
  - More memory efficient
  - Supports vectorized operations (no loops required)

---

## 2. Creating Arrays
### From Python List
```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
```

### Special Arrays
```python
np.zeros((3,3))       # 3x3 matrix of zeros
np.ones((2,4))        # 2x4 matrix of ones
np.arange(0,10,2)     # [0 2 4 6 8]
np.linspace(0,1,5)    # 5 numbers evenly spaced between 0 and 1
np.eye(4)             # Identity matrix (4x4)
```

---

## 3. Array Attributes
```python
arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)   # (2, 3)
print(arr.ndim)    # 2 (dimensions)
print(arr.size)    # 6 (elements)
print(arr.dtype)   # int64 (data type)
```

---

## 4. Indexing & Slicing
### 1D Arrays
```python
arr = np.array([10,20,30,40,50])
print(arr[0])    # 10
print(arr[-1])   # 50
print(arr[1:4])  # [20 30 40]
```

### 2D Arrays
```python
mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mat[0,0])      # 1
print(mat[1,:])      # [4 5 6] (second row)
print(mat[:,2])      # [3 6 9] (third column)
```

---

## 5. Array Operations
```python
arr = np.array([1,2,3,4,5])
print(arr + 5)       # [ 6  7  8  9 10]
print(arr * 2)       # [ 2  4  6  8 10]

print(np.mean(arr))  # 3.0
print(np.max(arr))   # 5
print(np.min(arr))   # 1
print(np.std(arr))   # 1.41...
```

Universal functions:
```python
print(np.sin(arr))
print(np.exp(arr))
print(np.sqrt(arr))
```

---

## 6. Reshaping & Stacking
```python
arr = np.arange(1,13)
print(arr.reshape(3,4))   # reshape into 3x4 matrix

a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.hstack([a,b]))   # [1 2 3 4 5 6]
print(np.vstack([a,b]))   # [[1 2 3]
                          #  [4 5 6]]
```

---

## 7. Boolean Indexing & Filtering
```python
arr = np.array([10,20,30,40,50])
print(arr[arr > 25])   # [30 40 50]
```

---

## 8. Random Module
```python
np.random.rand(3)          # [0.52 0.72 0.28]
np.random.randn(3,3)       # Normal distribution
np.random.randint(1,100,5) # 5 random integers
np.random.seed(42)         # Reproducible results
```

---

## 9. Broadcasting
```python
arr = np.array([1,2,3])
print(arr + 5)             # scalar broadcasting

mat = np.array([[1,2,3],[4,5,6]])
row = np.array([1,0,1])
print(mat + row)
```

---

## 10. Practice Exercises
1. Create a 5x5 matrix with values from 1–25.  
2. Slice out the middle 3x3 matrix.  
3. Generate 10 random integers between 1 and 100, then compute mean and standard deviation.  
4. Create two 3x3 arrays and compute their dot product.  
5. Demonstrate broadcasting with a 3x3 matrix and a 1D row vector.  

---
