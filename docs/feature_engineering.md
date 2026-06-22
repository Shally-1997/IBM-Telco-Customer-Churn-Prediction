# Feature Engineering Report

## Project: IBM Telco Customer Churn Prediction

### Objective

The purpose of feature engineering is to transform raw customer data into meaningful features that improve the predictive performance of machine learning models. This stage focuses on encoding categorical variables, creating business-driven features, and preparing the dataset for model training.

---

# Initial Dataset

The cleaned dataset obtained from the data cleaning phase contains customer demographic information, subscribed services, account details, and churn status.

### Target Variable

* **Churn**

  * Yes → 1
  * No → 0

This conversion transforms the target variable into a machine-learning-friendly numerical format.

---

# Binary Encoding

Several columns contain only Yes/No values.

### Encoded Features

* Partner
* Dependents
* PhoneService
* PaperlessBilling

### Transformation

| Original Value | Encoded Value |
| -------------- | ------------- |
| Yes            | 1             |
| No             | 0             |

### Purpose

Binary encoding reduces memory usage and allows machine learning algorithms to process categorical information efficiently.

---

# Gender Encoding

The gender column was converted into numerical values.

### Transformation

| Gender | Encoded Value |
| ------ | ------------- |
| Male   | 1             |
| Female | 0             |

### Purpose

Machine learning models require numerical inputs and cannot directly interpret text values.

---

# Feature Creation

## 1. Tenure Group

A new categorical feature called **TenureGroup** was created by segmenting customers based on the number of months they have stayed with the company.

### Groups

| Tenure (Months) | Group |
| --------------- | ----- |
| 0 – 12          | 0-12  |
| 12 – 24         | 12-24 |
| 24 – 48         | 24-48 |
| 48 – 72         | 48-72 |

### Business Importance

Customer behavior often differs significantly between new and long-term customers. Grouping tenure helps capture customer lifecycle stages.

---

## 2. Average Monthly Spend

### Formula

Average Monthly Spend = TotalCharges / (Tenure + 1)

### Purpose

This feature estimates the customer's average expenditure over their relationship with the company.

### Business Importance

Customers with higher spending patterns may have different churn behavior compared to low-spending customers.

---

## 3. High Value Customer

A new binary feature was created to identify customers with above-average monthly charges.

### Logic

If MonthlyCharges > Median(MonthlyCharges)

Then:

* 1 = High Value Customer
* 0 = Regular Customer

### Business Importance

High-value customers are often prioritized for retention efforts because of their greater revenue contribution.

---

## 4. Contract Length

The contract type was transformed into an ordinal feature.

### Mapping

| Contract Type  | Value |
| -------------- | ----- |
| Month-to-month | 0     |
| One year       | 1     |
| Two year       | 2     |

### Business Importance

Longer contract commitments generally indicate stronger customer loyalty and lower churn risk.

---

## 5. Total Services

A new feature was created to count the number of subscribed services.

### Services Considered

* PhoneService
* MultipleLines
* OnlineSecurity
* OnlineBackup
* DeviceProtection
* TechSupport
* StreamingTV
* StreamingMovies

### Purpose

This feature measures customer engagement with the company.

### Business Importance

Customers using more services are often less likely to switch providers because of higher switching costs.

---

## 6. Charge Per Service

### Formula

Charge Per Service = MonthlyCharges / (TotalServices + 1)

### Purpose

Measures the average amount paid for each subscribed service.

### Business Importance

This feature helps identify customers who may perceive services as expensive relative to the value received.

---

# Categorical Feature Identification

Remaining categorical variables were identified using data types for further encoding.

### Purpose

Categorical variables must be transformed before model training through techniques such as:

* One-Hot Encoding
* Ordinal Encoding
* Target Encoding

---

# Numerical Feature Identification

Key numerical features identified:

* tenure
* MonthlyCharges
* TotalCharges

### Purpose

Numerical features may later undergo scaling or normalization depending on the selected machine learning algorithm.

---

# Dataset Preparation

## Train-Test Split

The dataset was divided into training and testing sets.

### Configuration

* Test Size: 20%
* Random State: 42
* Stratification: Churn

### Purpose

Stratified sampling ensures that both training and testing datasets maintain the original churn distribution.

---

# Feature Engineering Summary

### Features Created

1. TenureGroup
2. AvgMonthlySpend
3. HighValueCustomer
4. ContractLength
5. TotalServices
6. ChargePerService

### Features Encoded

1. Churn
2. Partner
3. Dependents
4. PhoneService
5. PaperlessBilling
6. Gender

---

# Expected Impact on Model Performance

The engineered features are designed to capture:

* Customer loyalty
* Service adoption level
* Revenue contribution
* Spending behavior
* Contract commitment
* Customer value segmentation

These features provide additional business context beyond the original dataset and are expected to improve churn prediction performance.

---

# Conclusion

Feature engineering transformed raw customer information into meaningful predictors of churn. New business-driven features such as TotalServices, AvgMonthlySpend, ChargePerService, and ContractLength enhance the dataset's predictive power and prepare it for machine learning model development.
