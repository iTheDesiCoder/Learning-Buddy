# Multithreading in Python

---

## 🔹 What is Multithreading?
- **Thread** → a lightweight unit of execution within a process.  
- **Multithreading** allows multiple tasks to run "concurrently" within the same program.  
- Useful for **I/O-bound tasks** (e.g., file reading, API calls, database queries).  

⚠️ Note: Python has the **Global Interpreter Lock (GIL)** which limits true parallelism for CPU-bound tasks.  
For CPU-heavy tasks, use **multiprocessing** instead.  

---

## 🔹 Why Multithreading?
- Improves responsiveness.  
- Handles multiple tasks simultaneously (e.g., downloading files, serving clients).  
- Efficient for programs waiting on external resources.  

---

## 🔹 Creating Threads with `threading` Module
```python
import threading

def print_numbers():
    for i in range(5):
        print("Number:", i)

def print_letters():
    for ch in ['A', 'B', 'C', 'D', 'E']:
        print("Letter:", ch)

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

print("Done!")
```

---

## 🔹 Using `Lock` to Prevent Race Conditions
```python
import threading

balance = 0
lock = threading.Lock()

def deposit():
    global balance
    for _ in range(100000):
        with lock:  # ensures only one thread modifies balance at a time
            balance += 1

t1 = threading.Thread(target=deposit)
t2 = threading.Thread(target=deposit)

t1.start()
t2.start()
t1.join()
t2.join()

print("Final Balance:", balance)  # Expected: 200000
```

---

## 🔹 Using `concurrent.futures` (Simpler API)
```python
import concurrent.futures
import time

def task(n):
    time.sleep(1)
    return f"Task {n} done"

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, range(5))

for r in results:
    print(r)
```

Output:
```
Task 0 done
Task 1 done
Task 2 done
Task 3 done
Task 4 done
```

---

## 🔹 Multithreading vs Multiprocessing
- **Multithreading** → Best for I/O-bound tasks.  
- **Multiprocessing** → Best for CPU-bound tasks (parallel execution).  

```python
# Rule of thumb:
# I/O tasks → threading / async
# CPU tasks → multiprocessing
```

---

## 🔹 Real-World Example: Downloading Multiple URLs
```python
import threading
import requests

urls = [
    "https://www.example.com",
    "https://httpbin.org/get",
    "https://api.github.com"
]

def fetch(url):
    response = requests.get(url)
    print(f"{url}: {response.status_code}")

threads = []
for url in urls:
    t = threading.Thread(target=fetch, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
```

---

## 🔹 COBOL / Java / C# Mapping
| Concept | COBOL | Java / C# | Python |
|---------|-------|-----------|--------|
| Concurrency | Batch jobs (sequential) | `Thread`, `Executor`, `Task` | `threading`, `concurrent.futures` |
| Race Conditions | Not relevant | Synchronization (`synchronized`, `lock`) | `threading.Lock` |
| Thread Pools | Not available | ExecutorService, ThreadPool | `ThreadPoolExecutor` |

---

## 💡 Exercises
1. Write a program that creates two threads: one prints even numbers, another prints odd numbers up to 20.  
2. Create a shared counter updated by 5 threads. Use `Lock` to avoid race conditions.  
3. Use `ThreadPoolExecutor` to simulate downloading 5 files in parallel.  
4. Compare execution time of sequential vs threaded execution of a function that sleeps for 2 seconds.  

---
