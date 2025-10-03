# Chapter 1: DataFrames I – Introduction

In this chapter, we will introduce **Pandas DataFrames** and practice using our financial datasets:  
- **Customer.csv**  
- **Order.csv**  

---

## 1. Methods and Attributes between Series and DataFrames

### Example: Load Customer Data
```python
import pandas as pd

customers = pd.read_csv("Customer.csv")
print(customers.head())
print(customers.shape)   # rows, columns
print(customers.columns)
print(customers.dtypes)
```
Output (sample):
```
   AccountNumber        CustomerName State  AccountBalance
0           1001          John Smith    NJ           72236
1           1002        Emma Johnson    TX           95818
2           1003   Michael Williams    FL           87651
3           1004        Sophia Brown    MA           34067
4           1005         James Jones    PA           56431
```

---

## 2. Differences between Shared Methods

Both **Series** and **DataFrames** have methods like `.head()`, `.describe()`, etc.  
- Series applies them to a single column  
- DataFrame applies them to the whole table

```python
print(customers["AccountBalance"].mean())  # Series method
print(customers.describe())                # DataFrame method
```

---

## 3. Select One Column from a DataFrame
```python
print(customers["CustomerName"].head())
```

---

## 4. Select Multiple Columns
```python
print(customers[["CustomerName", "AccountBalance"]].head())
```

---

## 5. Add New Column
Add a column in `Order.csv` for total order value.

```python
orders = pd.read_csv("Order.csv")
orders["TotalValue"] = orders["Qty"] * orders["Price"]
print(orders.head())
```

Output (sample):
```
   AccountNumber  OrderNumber     Security  Qty   Price   OrderDate  TotalValue
0           1015         2001  Mutual Fund   58  377.46  2023-01-01   21892.68
1           1002         2002       Equity  377  112.90  2023-01-08   42561.30
```

---

## 6. Review of value_counts Method
```python
print(orders["Security"].value_counts())
```
Output:
```
Equity         37
Mutual Fund    34
Options        29
Name: Security, dtype: int64
```

---

## 7. Drop Rows with Missing Values
```python
orders_with_na = orders.copy()
orders_with_na.loc[5, "Qty"] = None

print(orders_with_na.dropna().head())
```

---

## 8. Fill Missing Values
```python
print(orders_with_na["Qty"].fillna(0).head())
```

---

## 9. The astype Method (Convert Data Types)
```python
orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])
print(orders.dtypes)
```

---

## 10. Sort a DataFrame with sort_values
```python
print(customers.sort_values("AccountBalance", ascending=False).head())
```

---

## 11. Sort by Index with sort_index
```python
print(customers.sort_index().head())
```

---

## 12. Rank Series Values with rank
```python
customers["BalanceRank"] = customers["AccountBalance"].rank(ascending=False)
print(customers.head())
```

---

# 📝 Practice Exercises
1. Show top 5 customers by AccountBalance.  
2. Add a new column to Orders for a 1% brokerage fee on `TotalValue`.  
3. Find how many orders are placed per Security type.  
4. Sort customers by CustomerName alphabetically.  
5. Rank customers based on their AccountBalance.
