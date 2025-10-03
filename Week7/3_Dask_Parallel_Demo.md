# Dask Tutorial – Parallelism and Scaling Beyond Pandas

In this tutorial, we will explore **Dask**, a powerful Python library for parallel and distributed computing.  
We will compare **Pandas vs Dask**, show how Dask executes tasks in parallel, and explain when to use it.

---

# 1. Why Dask?
- **Pandas**: Works well for small-to-medium datasets that fit in memory.  
- **Problem**: Large datasets (tens of GBs) do not fit in memory, and Pandas uses only **one CPU core**.  
- **Dask**: Splits the dataset into **partitions** (mini DataFrames) and runs them **in parallel** across multiple cores or even a cluster.  

👉 **Dask = Pandas at Scale.**  

---

# 2. Setting Up Dask Client and Dashboard

The `Client()` launches a local cluster. It also provides a **dashboard** to visualize parallel execution.

```python
from dask.distributed import Client

client = Client()
print(client)   # Shows cluster info and dashboard URL (http://localhost:8787)
```

👉 Open the printed dashboard URL in your browser to see **real-time tasks running**.

---

# 3. Compare Pandas vs Dask – Simple Example

```python
import pandas as pd
import dask.dataframe as dd

# Pandas
df_pandas = pd.read_csv("Order.csv")
print(df_pandas["Price"].mean())

# Dask
df_dask = dd.read_csv("Order.csv")
print(df_dask["Price"].mean().compute())
```

⚡ Notice: Dask requires `.compute()` because it builds a **task graph** lazily.

---

# 4. Create a Big Dataset for Benchmark

We create a synthetic dataset with 5 million rows to see the difference.

```python
import numpy as np

df = pd.DataFrame({
    "A": np.random.randint(0, 100, size=5_000_000),
    "B": np.random.rand(5_000_000)
})
df.to_csv("big.csv", index=False)
```

---

# 5. Load with Pandas vs Dask

```python
# Pandas (single core)
df_pandas = pd.read_csv("big.csv")
print(df_pandas["B"].mean())

# Dask (multi-core)
df_dask = dd.read_csv("big.csv")
print(df_dask["B"].mean().compute())
```

👉 Pandas uses **1 core**, Dask uses **all cores**.  
Check the Dask Dashboard or Task Manager to see parallelism.

---

# 6. Parallel GroupBy Example

```python
# Pandas
print(df_pandas.groupby("A")["B"].mean())

# Dask
print(df_dask.groupby("A")["B"].mean().compute())
```

In Dask, each partition is grouped **in parallel**, then results are combined.

---

# 7. Visualizing the Task Graph

Dask allows us to visualize execution as a **Directed Acyclic Graph (DAG)**.

```python
df_dask.groupby("A")["B"].mean().visualize(filename="task_graph.png")
```

👉 This generates a `task_graph.png` file showing parallel execution.

---

# 8. When to Use Dask?

- Dataset is **too large to fit in memory**.  
- You want to **use multiple CPU cores** for speed.  
- You want the same code to run on a **laptop or a distributed cluster**.  
- You need **lazy evaluation** for optimized workflows.

---

# 📝 Practice Exercises

1. Load `big.csv` with both Pandas and Dask, compare runtime for `.mean()`.  
2. Use Dask to compute **total order value per SecurityType** in `Order.csv`.  
3. Count the number of unique SecurityNames using Dask.  
4. Run a `.groupby()` in Dask and open the dashboard to show parallel partitions.  
5. Generate and inspect a Dask task graph using `.visualize()`.  

---
