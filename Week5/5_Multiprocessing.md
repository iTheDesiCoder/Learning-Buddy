# Multiprocessing in Python

---

## 🔹 What is Multiprocessing?
- **Multiprocessing** allows a program to run multiple **independent processes** simultaneously.  
- Each process has its **own Python interpreter** and **memory space**.  
- Unlike threads, multiprocessing is not limited by the **Global Interpreter Lock (GIL)**.  
- Best for **CPU-bound tasks** (e.g., calculations, data crunching).  

---

## 🔹 Why Multiprocessing?
- True parallel execution on multiple CPU cores.  
- Ideal for heavy computations (e.g., math operations, simulations, ML training).  
- Solves the GIL limitation of threads.  

---

## 🔹 Creating Processes with `multiprocessing.Process`
```python
from multiprocessing import Process

def task(name):
    print(f"Running {name}")

if __name__ == "__main__":
    p1 = Process(target=task, args=("Process-1",))
    p2 = Process(target=task, args=("Process-2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("All processes finished!")
```

---

## 🔹 Sharing Data with `Queue`
Processes do not share memory. Use `Queue` for communication.  

```python
from multiprocessing import Process, Queue

def worker(q, n):
    q.put(n * n)

if __name__ == "__main__":
    q = Queue()
    processes = [Process(target=worker, args=(q, i)) for i in range(5)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    results = [q.get() for _ in range(5)]
    print("Squares:", results)
```

Output:
```
Squares: [0, 1, 4, 9, 16]
```

---

## 🔹 Sharing Data with `Value` and `Array`
```python
from multiprocessing import Process, Value, Array

def add_one(val, arr):
    val.value += 1
    for i in range(len(arr)):
        arr[i] += 1

if __name__ == "__main__":
    val = Value('i', 0)          # integer
    arr = Array('i', [1, 2, 3])  # array of integers

    p = Process(target=add_one, args=(val, arr))
    p.start()
    p.join()

    print("Value:", val.value)   # 1
    print("Array:", arr[:])      # [2, 3, 4]
```

---

## 🔹 Using `Pool` for Parallel Execution
```python
from multiprocessing import Pool

def square(n):
    return n * n

if __name__ == "__main__":
    with Pool(4) as pool:  # 4 processes
        results = pool.map(square, range(10))
    print(results)
```

Output:
```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

---

## 🔹 Using `concurrent.futures.ProcessPoolExecutor`
```python
import concurrent.futures

def cube(n):
    return n ** 3

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(cube, range(6)))
    print(results)
```

Output:
```
[0, 1, 8, 27, 64, 125]
```

---

## 🔹 Multiprocessing vs Multithreading

| Feature | Multithreading | Multiprocessing |
|---------|----------------|-----------------|
| Execution | Concurrent, but limited by GIL | True parallel execution |
| Best for | I/O-bound tasks | CPU-bound tasks |
| Memory | Shared | Separate per process |
| Overhead | Lightweight | Higher (separate interpreter & memory) |
| Example | Reading multiple files | Heavy math, ML training |

---

## 🔹 COBOL / Java / C# Mapping
| Concept | COBOL | Java / C# | Python |
|---------|-------|-----------|--------|
| Parallel Processing | Multiple batch jobs (JCL steps) | ForkJoinPool, Task Parallel Library | `multiprocessing`, `ProcessPoolExecutor` |
| Shared Memory | Not typical | `volatile`, locks | `Value`, `Array`, `Queue` |
| CPU Utilization | Sequential execution | Multi-core support | Fully uses multiple cores |

---

## 💡 Exercises
1. Write a program that spawns 4 processes to calculate squares of numbers 1–10.  
2. Use `Queue` to send data from worker processes back to the main process.  
3. Compare execution time of calculating factorial of large numbers using sequential vs multiprocessing.  
4. Extend `BankAccount` to simulate deposits using multiple processes with a shared `Value`.  

---
