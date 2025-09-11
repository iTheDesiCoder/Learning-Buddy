# Multithreading with File Processing in Python

---

## 🔹 Why File Processing with Multithreading?
- In COBOL, file processing is typically **sequential** (record by record).  
- In Python, we can use **multithreading** to speed up file processing, especially for **large files**.  
- Useful for:  
  - Log analysis  
  - Transaction files  
  - CSV data parsing  

---

## 🔹 Sequential File Processing (Baseline)
```python
def process_file(filename):
    with open(filename, "r") as f:
        for line in f:
            print(f"Processed: {line.strip()}")

process_file("data.txt")
```

⚠️ Limitation → Each line is processed **one after another**.  

---

## 🔹 Splitting Work into Threads
- Break file into chunks.  
- Assign each chunk to a thread.  

```python
import threading

def process_lines(lines):
    for line in lines:
        print(f"{threading.current_thread().name} processed: {line.strip()}")

def threaded_file_processing(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    chunk_size = len(lines) // 4  # 4 threads
    threads = []

    for i in range(0, len(lines), chunk_size):
        t = threading.Thread(target=process_lines, args=(lines[i:i+chunk_size],))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

threaded_file_processing("data.txt")
```

---

## 🔹 Using `concurrent.futures` (ThreadPool)
- Cleaner API.  
- Automatically manages threads.  

```python
import concurrent.futures
import threading

def process_line(line):
    return f"{threading.current_thread().name} processed: {line.strip()}"

def process_file_threaded(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(process_line, lines)

    for r in results:
        print(r)

process_file_threaded("data.txt")
```

---

## 🔹 Real-World Example: Processing Transactions (CSV)
```python
import concurrent.futures
import threading
import csv

def process_transaction(row):
    account, amount = row
    return f"{threading.current_thread().name}: Account {account} processed {amount}"

with open("transactions.csv", "r") as f:
    reader = list(csv.reader(f))

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(process_transaction, reader)

for r in results:
    print(r)
```

Example CSV (`transactions.csv`):
```
1001,500
1002,300
1003,700
```

Output:
```
ThreadPoolExecutor-0_0: Account 1001 processed 500
ThreadPoolExecutor-0_1: Account 1002 processed 300
ThreadPoolExecutor-0_2: Account 1003 processed 700
```

---

## 🔹 When to Use Multithreading for Files
✅ Best for:  
- Large text/CSV files  
- I/O-heavy tasks (reading + network/db calls)  
❌ Not useful for:  
- CPU-heavy parsing (use multiprocessing instead)  

---

## 🔹 COBOL / Java / C# Mapping
| Concept | COBOL | Java / C# | Python |
|---------|-------|-----------|--------|
| File Processing | `READ NEXT RECORD` sequential | `BufferedReader`, `StreamReader` | `open()`, `readlines()` |
| Multithreaded File Processing | Not available | ExecutorService + File I/O | `threading`, `ThreadPoolExecutor` |
| Batch Job Parallelism | Multiple JCL steps | Parallel Streams (Java 8) | ThreadPool / multiprocessing |

---

## 💡 Exercises
1. Read a file with 100 lines and process it using 4 threads. Print which thread processed each line.  
2. Write a CSV file `employees.csv` with columns `id,name,salary`. Process it in multiple threads and print employees with salary > 5000.  
3. Extend the `BankAccount` class to process transactions from a CSV file using multithreading.  
4. Compare execution time of sequential vs threaded processing for a file with 10,000 lines.  

---
