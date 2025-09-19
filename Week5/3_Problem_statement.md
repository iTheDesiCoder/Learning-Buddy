# Week 5: Why Multithreading & Parallel Processing?
**Audience:** Python learners who have built small apps and now need to scale performance and responsiveness.  
**Goal:** Establish *why* concurrency matters before learning *how* to use it.

---

## 1) The Problem Statement (in plain English)
> Our programs feel **slow** or **unresponsive** because they do **one thing at a time**.  
> When tasks involve **waiting for external resources** (web, disk, DB) or **heavy computation** (math, image/video, ML), the one-at-a-time model **wastes time** and **blocks user experience**.

**Two common pain categories:**
- **I/O-bound:** Time is spent *waiting* (network calls, file reads/writes, DB queries). CPU is mostly idle.
- **CPU-bound:** Time is spent *computing* (image transforms, compression, simulations). CPU is maxed out.

**We need tools that:**
- Keep the app responsive (don’t freeze the UI/server).
- Shorten total runtime of batches (e.g., download 100 pages, process 1000 images).
- Use hardware effectively (multiple cores, fast context switches).

---

## 2) Sequential Baseline (Status Quo)
**Symptoms of the problem:**
- A script that downloads 50 URLs **one by one**: total time ≈ sum of all waits.
- An analytics job crunching large arrays **in a single process**: total time ≈ sum of all CPU work on **one core**.
- A web server handling requests **serially**: one slow request blocks others.

```python

import time

start_time = time.time()

total = 0
count = 0

with open("scores.txt", "r") as f:
    for line in f:
        name, score = line.strip().split(",")
        total += int(score)
        count += 1
        time.sleep(0.001)  # 1 millisecond pause per line
average = total / count
print("Average Score:", average)

end_time = time.time()
print("Time taken:", end_time - start_time, "seconds")
```


