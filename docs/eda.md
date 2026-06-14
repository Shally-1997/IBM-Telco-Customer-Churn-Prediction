# Exploratory Data Analysis (EDA) Report

## Project: IBM Telco Customer Churn Prediction

### Objective

The goal of this analysis is to understand customer behavior and identify factors associated with customer churn. Insights from this EDA will guide feature selection and model development for predicting whether a customer is likely to leave the telecom company.

---

# Dataset Overview

* Total Records: **7,032**
* Total Features: **20**
* Missing Values in `TotalCharges`: **0**
* Target Variable: **Churn**

### Churn Distribution

| Churn Status | Count |
| ------------ | ----- |
| No           | 5,163 |
| Yes          | 1,869 |

### Churn Percentage

* Customers Retained: **73%**
* Customers Churned: **27%**

### Observation

The dataset is moderately imbalanced, with approximately one out of every four customers leaving the company. This indicates that churn prediction is an important business problem because retaining existing customers is generally less expensive than acquiring new ones.

---

# Univariate Analysis

## Monthly Charges Distribution

### Visualization

Histogram with KDE curve

### Observations

* Monthly charges are spread across a wide range.
* Most customers fall within the medium charge range.
* The distribution suggests the presence of different customer segments based on service subscriptions.

### Business Insight

Customers paying higher monthly charges may have different churn behavior compared to those paying lower charges.

---

# Bivariate Analysis

## 1. Churn vs Gender

### Observations

* Male and female customers show similar churn patterns.
* No significant difference is visible between genders.

### Business Insight

Gender alone is unlikely to be a strong predictor of customer churn.

---

## 2. Churn vs Senior Citizen

### Observations

* Senior citizens appear to have a relatively higher churn proportion compared to non-senior customers.
* The percentage of churned customers is visibly larger among senior citizens.

### Business Insight

Senior citizens may require specialized retention strategies and customer support services.

---

## 3. Churn vs Contract Type

### Observations

* Month-to-month contract customers show the highest churn.
* One-year contract customers churn less frequently.
* Two-year contract customers have the lowest churn rate.

### Business Insight

Contract duration is one of the strongest indicators of churn.

Customers with long-term commitments are significantly less likely to leave.

### Recommendation

Encourage customers to move from month-to-month contracts to annual or multi-year plans through discounts and loyalty programs.

---

## 4. Churn vs Internet Service

### Observations

* Churn behavior varies across internet service types.
* Fiber optic customers tend to exhibit higher churn compared to DSL customers.
* Customers without internet services show lower churn.

### Business Insight

Service quality, pricing, or customer expectations associated with fiber optic plans may influence churn.

### Recommendation

Investigate customer satisfaction among fiber optic subscribers.

---

## 5. Churn vs Payment Method

### Observations

* Electronic check customers appear to have higher churn rates.
* Customers using automatic payment methods show lower churn.

### Business Insight

Customers enrolled in automatic payment systems are generally more stable and engaged.

### Recommendation

Promote automatic payment enrollment through incentives and discounts.

---

# Numerical Feature Analysis

## 6. Monthly Charges vs Churn

### Visualization

Box Plot

### Observations

* Churned customers generally have higher monthly charges.
* The median monthly charge is greater for customers who left.

### Business Insight

Higher service costs may contribute to customer dissatisfaction and eventual churn.

### Recommendation

Review pricing structures and offer personalized plans for high-paying customers.

---

## 7. Tenure vs Churn

### Visualization

Box Plot

### Observations

* Customers who churn typically have lower tenure.
* Long-term customers are more likely to stay.

### Business Insight

Customer loyalty increases over time.

The first few months of a customer's lifecycle are critical for retention.

### Recommendation

Implement onboarding programs and engagement campaigns targeting new customers.

---

## 8. Total Charges vs Churn

### Visualization

Box Plot

### Observations

* Churned customers generally have lower total charges.
* Customers with higher total charges tend to remain with the company.

### Business Insight

Higher total charges often correspond to longer tenure and stronger customer relationships.

### Recommendation

Focus retention efforts on customers with low tenure and lower accumulated spending.

---

# Key Findings

The following factors appear to have the strongest relationship with customer churn:

### High Impact Features

1. Contract Type
2. Tenure
3. Monthly Charges
4. Payment Method
5. Internet Service
6. Senior Citizen Status

### Low Impact Features

1. Gender

---

# Business Recommendations

### Customer Retention Strategy

* Encourage long-term contracts.
* Improve retention during the first year of customer lifecycle.
* Monitor high monthly charge customers.
* Promote automatic payment methods.
* Investigate churn among fiber optic customers.
* Design targeted programs for senior citizens.

---

# Conclusion

The EDA reveals that customer churn is primarily influenced by contract commitment, tenure, pricing, and payment behavior. Customers on month-to-month contracts, with shorter tenure and higher monthly charges, are significantly more likely to leave the company.

These findings will guide the feature engineering and machine learning stages of the churn prediction project.
