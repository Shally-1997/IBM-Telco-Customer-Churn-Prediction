# Data Dictionary

## Dataset Overview

This dataset contains customer demographic information, account details, subscribed services, billing information, and churn status. It is used to predict whether a customer is likely to leave the telecom company.

### Dataset Information

| Attribute       | Value                    |
| --------------- | ------------------------ |
| Dataset Name    | IBM Telco Customer Churn |
| Total Records   | 7,043                    |
| Total Features  | 21                       |
| Target Variable | Churn                    |
| File Format     | CSV                      |

---

## Feature Description

| Column Name      | Data Type       | Description                                                          |
| ---------------- | --------------- | -------------------------------------------------------------------- |
| customerID       | String          | Unique identifier assigned to each customer                          |
| gender           | Categorical     | Gender of the customer (Male/Female)                                 |
| SeniorCitizen    | Binary          | Indicates whether the customer is a senior citizen (1 = Yes, 0 = No) |
| Partner          | Categorical     | Whether the customer has a partner (Yes/No)                          |
| Dependents       | Categorical     | Whether the customer has dependents (Yes/No)                         |
| tenure           | Integer         | Number of months the customer has stayed with the company            |
| PhoneService     | Categorical     | Whether the customer has phone service                               |
| MultipleLines    | Categorical     | Whether the customer has multiple phone lines                        |
| InternetService  | Categorical     | Type of internet service (DSL, Fiber Optic, No)                      |
| OnlineSecurity   | Categorical     | Whether online security service is subscribed                        |
| OnlineBackup     | Categorical     | Whether online backup service is subscribed                          |
| DeviceProtection | Categorical     | Whether device protection service is subscribed                      |
| TechSupport      | Categorical     | Whether technical support service is subscribed                      |
| StreamingTV      | Categorical     | Whether streaming TV service is subscribed                           |
| StreamingMovies  | Categorical     | Whether streaming movie service is subscribed                        |
| Contract         | Categorical     | Contract type (Month-to-Month, One Year, Two Year)                   |
| PaperlessBilling | Categorical     | Whether paperless billing is enabled                                 |
| PaymentMethod    | Categorical     | Customer payment method                                              |
| MonthlyCharges   | Float           | Monthly amount charged to the customer                               |
| TotalCharges     | Float           | Total amount charged during customer tenure                          |
| Churn            | Target Variable | Whether the customer left the company (Yes/No)                       |

---

## Target Variable

### Churn

| Value | Meaning                              |
| ----- | ------------------------------------ |
| Yes   | Customer has left the company        |
| No    | Customer is still an active customer |

---

## Feature Categories

### Demographic Features

* gender
* SeniorCitizen
* Partner
* Dependents

### Account Features

* tenure
* Contract
* PaperlessBilling
* PaymentMethod

### Service Features

* PhoneService
* MultipleLines
* InternetService
* OnlineSecurity
* OnlineBackup
* DeviceProtection
* TechSupport
* StreamingTV
* StreamingMovies

### Billing Features

* MonthlyCharges
* TotalCharges

### Target Feature

* Churn

---

## Data Quality Notes

1. `customerID` would not be used for model training.
2. `TotalCharges` may contain missing or blank values and would be cleaned before analysis.
3. Categorical variables would be encoded before machine learning model training.
4. The target variable `Churn` would be converted into binary format:

   * Yes → 1
   * No → 0

---

## Business Objective

The objective of this project is to identify customers who are likely to churn and understand the factors influencing customer retention. Insights from this model can help telecom companies reduce customer attrition and improve customer satisfaction.
