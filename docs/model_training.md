# Model Building & Evaluation Report

# IBM Telco Customer Churn Prediction

---

# Objective

The objective of the model building phase is to develop machine learning models capable of predicting customer churn accurately. Multiple classification algorithms were trained and compared to identify the model that best balances churn detection and overall performance.

Because customer churn is an imbalanced classification problem, the primary focus was not only on overall accuracy but also on the model's ability to correctly identify churning customers (Recall for Class 1).

---

# Machine Learning Workflow

The complete machine learning workflow followed these steps:

1. Train-Test Split
2. Data Preprocessing using ColumnTransformer
3. Building Pipelines
4. Training Multiple Models
5. Hyperparameter Tuning
6. Model Evaluation
7. Model Comparison
8. Feature Importance Analysis
9. Final Model Selection

---

# Train-Test Split

The dataset was divided into:

* Training Data: 80%
* Testing Data: 20%

Parameters used:

```python
test_size = 0.2
random_state = 42
stratify = y
```

## Why Stratify?

The dataset contains approximately:

* 73% Non-Churn Customers
* 27% Churn Customers

Using stratified sampling ensures both training and testing datasets preserve the original class distribution.

Without stratification, one dataset may contain significantly fewer churn customers, resulting in biased model evaluation.

---

# Data Preprocessing

Machine learning algorithms require numerical inputs.

The preprocessing pipeline consisted of:

### Numerical Features

* StandardScaler()

Purpose:

* Normalize numerical variables
* Mean becomes 0
* Standard deviation becomes 1

This particularly benefits:

* Logistic Regression
* Support Vector Machines
* Neural Networks

Tree-based algorithms do not require scaling, but the same preprocessing pipeline was maintained for consistency.

---

### Categorical Features

OneHotEncoder()

Purpose:

Convert categorical variables into binary columns.

Example:

Contract

Month-to-month

One year

Two year

becomes

Contract_Month-to-month

Contract_One year

Contract_Two year

---

# Why ColumnTransformer?

Different preprocessing techniques are required for different feature types.

Instead of manually preprocessing each feature, ColumnTransformer performs:

* Scaling for numerical columns
* One-Hot Encoding for categorical columns

inside a single preprocessing pipeline.

Advantages:

* Cleaner code
* No data leakage
* Easy deployment
* Reproducible workflow

---

# Why Pipeline?

A Pipeline combines preprocessing and model training into one object.

Example:

Raw Data

↓

Preprocessing

↓

Model

↓

Prediction

Benefits:

* Prevents train-test leakage
* Simplifies hyperparameter tuning
* Easier deployment
* Production-ready workflow

---

# Models Trained

The following models were trained:

## 1. Logistic Regression

Characteristics:

* Linear classification algorithm
* Fast training
* Highly interpretable
* Works well on linearly separable data

Advantages:

* Easy to explain
* Baseline model
* Computationally efficient

Limitations:

* Cannot capture complex nonlinear relationships.

---

## 2. Decision Tree

Characteristics:

* Rule-based classifier
* Easy to visualize
* Handles nonlinear relationships

Advantages:

* Highly interpretable
* No feature scaling required

Limitations:

* Prone to overfitting
* High variance

---

## 3. Random Forest

Random Forest combines multiple Decision Trees.

Advantages:

* Reduces overfitting
* Better generalization
* Handles missing interactions
* More robust than a single tree

Random Forest was trained in three configurations:

* Default Parameters
* GridSearchCV
* RandomizedSearchCV

---

## 4. XGBoost

XGBoost is an optimized gradient boosting algorithm.

Advantages:

* Handles nonlinear relationships
* Regularization reduces overfitting
* High predictive performance
* Industry standard for structured/tabular datasets

Limitations:

* Slower training
* More hyperparameters
* More difficult to interpret

---

# Hyperparameter Tuning

Two tuning techniques were used.

## GridSearchCV

GridSearchCV evaluates every possible parameter combination.

Example:

```
max_depth

5

10

15

None

n_estimators

100

200

300
```

Every combination is evaluated.

Advantages:

* Finds the optimal parameters

Disadvantages:

* Computationally expensive.

---

## RandomizedSearchCV

RandomizedSearchCV randomly samples combinations from the search space.

Advantages:

* Much faster
* Handles large parameter spaces
* Often achieves similar performance to GridSearchCV

---

# Why ROC-AUC was used for Hyperparameter Tuning

Accuracy is not an ideal metric for imbalanced datasets.

Example:

If 73% of customers do not churn,

a model predicting

"No"

for everyone achieves

73% accuracy

without identifying a single churning customer.

ROC-AUC measures the model's ability to distinguish between churn and non-churn customers across different classification thresholds.

Higher ROC-AUC indicates better ranking ability.

Therefore ROC-AUC was selected as the optimization metric during hyperparameter tuning.

---

# Evaluation Metrics

## Accuracy

Measures overall prediction correctness.

Formula:

Accuracy = Correct Predictions / Total Predictions

Limitation:

Can be misleading on imbalanced datasets.

---

## Precision

Question answered:

Out of all predicted churn customers,

how many actually churned?

High precision means fewer False Positives.

---

## Recall

Question answered:

Out of all actual churn customers,

how many did the model correctly identify?

High recall means fewer False Negatives.

For churn prediction,

Recall is generally the most important metric because missing a customer likely to churn means losing potential revenue.

---

## F1 Score

F1 Score balances Precision and Recall.

Useful when both metrics are important.

---

## ROC-AUC

Measures the model's ability to rank positive samples higher than negative samples.

Range:

0.5 → Random Guess

1.0 → Perfect Classifier

Higher values indicate better discrimination.

---

# Model Comparison

| Model                              | Accuracy | Precision (Class 1) | Recall (Class 1) | F1 Score |
| ---------------------------------- | -------- | ------------------- | ---------------- | -------- |
| Logistic Regression                | 0.80     | 0.64                | 0.53             | 0.58     |
| Decision Tree                      | 0.73     | 0.49                | 0.51             | 0.50     |
| Random Forest (Default)            | 0.78     | 0.62                | 0.50             | 0.55     |
| Random Forest (GridSearchCV)       | 0.74     | 0.51                | 0.78             | 0.62     |
| Random Forest (RandomizedSearchCV) | 0.74     | 0.51                | 0.80             | 0.62     |
| XGBoost (GridSearchCV)             | 0.79     | 0.62                | 0.53             | 0.57     |

---

# Interpretation of Results

## Logistic Regression

* Highest overall accuracy.
* Good baseline performance.
* Missed many churn customers because recall was relatively low.

Suitable when overall prediction accuracy is the priority.

---

## Decision Tree

* Lower overall performance.
* Likely overfitted the training data.
* Weak recall and precision.

Not selected.

---

## Random Forest (Default)

* Better generalization than Decision Tree.
* Good balance of metrics.
* Recall remained moderate.

---

## Random Forest (GridSearchCV)

After tuning:

* Recall increased from 0.50 to 0.78.
* More churning customers were identified.
* Precision decreased because more non-churn customers were incorrectly classified as churn.

---

## Random Forest (RandomizedSearchCV)

This model achieved the highest Recall (0.80) among all evaluated models.

Although accuracy decreased slightly, the model became significantly better at identifying customers likely to churn.

This trade-off is acceptable because the business objective is to minimize customer loss.

---

## XGBoost

Produced strong overall performance.

However,

Recall remained lower than the tuned Random Forest model.

Therefore it was not selected as the final model despite achieving high accuracy.

---

# Final Model Selection

The final model selected was:

**Random Forest (RandomizedSearchCV)**

Reasons:

* Highest Recall (0.80)
* Best churn detection capability
* Balanced overall performance
* Reduced risk of missing churning customers
* Suitable for customer retention strategies

---

# Business Impact

A telecom company loses revenue whenever a customer churns.

Missing a churning customer (False Negative) means:

* Lost customer
* Lost recurring revenue
* Increased acquisition cost for replacement customers

The selected Random Forest model identifies approximately 80% of churning customers, enabling the business to proactively target at-risk customers with retention offers.

---

# Interview Questions Based on This Project

### Why did you use Pipeline?

To prevent data leakage, simplify preprocessing and model training, and make the workflow reproducible and deployment-ready.

---

### Why ColumnTransformer?

To apply different preprocessing techniques to numerical and categorical features within a single pipeline.

---

### Why did Random Forest outperform Decision Tree?

Random Forest averages predictions from multiple trees, reducing overfitting and improving generalization.

---

### Why optimize using ROC-AUC but select based on Recall?

ROC-AUC evaluates a model's overall ability to separate classes during tuning, independent of a specific threshold. After tuning, the business objective—identifying as many churning customers as possible—made Recall the deciding metric for final model selection.

---

### Why not choose the highest Accuracy model?

Accuracy can hide poor performance on the minority class. In churn prediction, correctly identifying customers who will leave is more valuable than maximizing overall accuracy.

---

### Why did Precision decrease after tuning?

Increasing Recall causes the model to predict more customers as churn. This captures more actual churners but also increases False Positives, lowering Precision. This is a common trade-off in classification.

---

### What is the biggest takeaway from this project?

Business objectives should guide model selection. The best model is not necessarily the one with the highest accuracy, but the one that best aligns with the problem—in this case, maximizing churn detection to support customer retention.
