# Data Cleaning Summary

## Overview

The IBM Telco Customer Churn dataset was cleaned and validated to ensure data quality before Exploratory Data Analysis (EDA) and machine learning model development.

---

## 1. Data Type Correction

### Issue

The `TotalCharges` column was stored as an `object` (string) instead of a numeric data type.

### Solution

Converted the column to numeric format using:

```python
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
```

### Outcome

* Numeric values were successfully converted.
* Invalid entries (blank spaces) were converted to `NaN`.

---

## 2. Missing Values in TotalCharges

### Issue

After conversion, 11 missing values were detected in the `TotalCharges` column.

### Reason

These records corresponded to customers with very low tenure and blank values in the original dataset.

### Solution

Removed rows containing missing values:

```python
df.dropna(inplace=True)
```

### Outcome

* Rows before cleaning: **7043**
* Rows after removing missing values: **7032**
* Missing values remaining: **0**

---

## 3. Duplicate Records Check

### Issue

Potential duplicate records needed to be verified.

### Validation Performed

```python
df.duplicated().sum()
```

### Result

```python
0
```

No duplicate rows were found in the original dataset.

---

## 4. Customer ID Uniqueness Check

### Validation Performed

```python
df["customerID"].duplicated().sum()
```

### Result

```python
0
```

Each customer record had a unique customer identifier.

---

## 5. Duplicate Check After Removing customerID

### Observation

After dropping the `customerID` column, 22 duplicate rows were detected.

```python
df.drop("customerID", axis=1).duplicated().sum()
```

### Result

```python
22
```

### Explanation

These records represent different customers who share identical values across all remaining features. Since the original dataset contains unique customer IDs and no true duplicate customer records, these observations were considered valid.

### Decision

The 22 records were **retained** and not removed because they represent legitimate customers rather than duplicated entries.

---

## 6. Removal of customerID

### Reason

The `customerID` column is a unique identifier and does not contribute to churn prediction.

### Solution

```python
df.drop("customerID", axis=1, inplace=True)
```

### Outcome

The column was removed before model development.

---

## Final Dataset Summary

| Metric                                    | Value |
| ----------------------------------------- | ----- |
| Original Rows                             | 7043  |
| Original Columns                          | 21    |
| Rows Removed (Missing TotalCharges)       | 11    |
| Duplicate Rows Removed                    | 0     |
| Final Rows                                | 7032  |
| Final Columns (after dropping customerID) | 20    |
| Missing Values Remaining                  | 0     |

---

## Conclusion

The dataset was successfully cleaned by correcting data types, handling missing values, validating duplicates, and removing the non-informative customer identifier column. The final dataset contains **7032 customer records and 20 predictive features**, making it suitable for exploratory data analysis and machine learning model development.
