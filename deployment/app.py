import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# Page Configuration

st.set_page_config(
    page_title="IBM Telco Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# Load Model

MODEL_PATH = Path(__file__).parent / "best_rf_model.pkl"

st.write("Model path:", MODEL_PATH)
st.write("Exists:", MODEL_PATH.exists())

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

# Title

st.title("📊 IBM Telco Customer Churn Prediction")

st.write(
    """
Predict whether a customer is likely to churn based on
their subscription details.

**Model Used:** Random Forest (Tuned)

"""
)

# Sidebar

st.sidebar.header("Customer Information")

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

SeniorCitizen = st.sidebar.selectbox(
    "Senior Citizen",
    ["No", "Yes"]
)

Partner = st.sidebar.selectbox(
    "Partner",
    ["No", "Yes"]
)

Dependents = st.sidebar.selectbox(
    "Dependents",
    ["No", "Yes"]
)

tenure = st.sidebar.slider(
    "Tenure (Months)",
    0,
    72,
    12
)

PhoneService = st.sidebar.selectbox(
    "Phone Service",
    ["No", "Yes"]
)

MultipleLines = st.sidebar.selectbox(
    "Multiple Lines",
    [
        "No",
        "Yes",
        "No phone service"
    ]
)

InternetService = st.sidebar.selectbox(
    "Internet Service",
    [
        "DSL",
        "Fiber optic",
        "No"
    ]
)

OnlineSecurity = st.sidebar.selectbox(
    "Online Security",
    [
        "No",
        "Yes",
        "No internet service"
    ]
)

OnlineBackup = st.sidebar.selectbox(
    "Online Backup",
    [
        "No",
        "Yes",
        "No internet service"
    ]
)

DeviceProtection = st.sidebar.selectbox(
    "Device Protection",
    [
        "No",
        "Yes",
        "No internet service"
    ]
)

TechSupport = st.sidebar.selectbox(
    "Tech Support",
    [
        "No",
        "Yes",
        "No internet service"
    ]
)

StreamingTV = st.sidebar.selectbox(
    "Streaming TV",
    [
        "No",
        "Yes",
        "No internet service"
    ]
)

StreamingMovies = st.sidebar.selectbox(
    "Streaming Movies",
    [
        "No",
        "Yes",
        "No internet service"
    ]
)

Contract = st.sidebar.selectbox(
    "Contract",
    [
        "Month-to-month",
        "One year",
        "Two year"
    ]
)

PaperlessBilling = st.sidebar.selectbox(
    "Paperless Billing",
    [
        "No",
        "Yes"
    ]
)

PaymentMethod = st.sidebar.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

MonthlyCharges = st.sidebar.number_input(
    "Monthly Charges",
    0.0,
    200.0,
    70.0
)

TotalCharges = st.sidebar.number_input(
    "Total Charges",
    0.0,
    10000.0,
    1000.0
)

# Feature Engineering

if tenure <= 12:
    TenureGroup = "0-12"
elif tenure <= 24:
    TenureGroup = "12-24"
elif tenure <= 48:
    TenureGroup = "24-48"
else:
    TenureGroup = "48-72"

AvgMonthlySpend = (
    TotalCharges / tenure
    if tenure != 0
    else MonthlyCharges
)

ContractLength = {
    "Month-to-month":1,
    "One year":12,
    "Two year":24
}[Contract]

TotalServices = sum([
    PhoneService=="Yes",
    MultipleLines=="Yes",
    InternetService!="No",
    OnlineSecurity=="Yes",
    OnlineBackup=="Yes",
    DeviceProtection=="Yes",
    TechSupport=="Yes",
    StreamingTV=="Yes",
    StreamingMovies=="Yes"
])

ChargePerService = MonthlyCharges / (TotalServices + 1)

High_value_customer = int(MonthlyCharges > 70)

# Binary Encoding

gender = 1 if gender=="Male" else 0
SeniorCitizen = 1 if SeniorCitizen=="Yes" else 0
Partner = 1 if Partner=="Yes" else 0
Dependents = 1 if Dependents=="Yes" else 0
PhoneService = 1 if PhoneService=="Yes" else 0
PaperlessBilling = 1 if PaperlessBilling=="Yes" else 0

# Input DataFrame

input_df = pd.DataFrame({

    "gender":[gender],
    "SeniorCitizen":[SeniorCitizen],
    "Partner":[Partner],
    "Dependents":[Dependents],
    "tenure":[tenure],
    "PhoneService":[PhoneService],
    "MultipleLines":[MultipleLines],
    "InternetService":[InternetService],
    "OnlineSecurity":[OnlineSecurity],
    "OnlineBackup":[OnlineBackup],
    "DeviceProtection":[DeviceProtection],
    "TechSupport":[TechSupport],
    "StreamingTV":[StreamingTV],
    "StreamingMovies":[StreamingMovies],
    "Contract":[Contract],
    "PaperlessBilling":[PaperlessBilling],
    "PaymentMethod":[PaymentMethod],
    "MonthlyCharges":[MonthlyCharges],
    "TotalCharges":[TotalCharges],
    "TenureGroup":[TenureGroup],
    "AvgMonthlySpend":[AvgMonthlySpend],
    "High_value_customer":[High_value_customer],
    "ContractLength":[ContractLength],
    "TotalServices":[TotalServices],
    "ChargePerService":[ChargePerService]

})

# Prediction

if st.button("Predict Churn"):

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:

        st.error("⚠ Customer is likely to Churn")

    else:

        st.success("✅ Customer is likely to Stay")

    st.metric(
        "Churn Probability",
        f"{probability*100:.2f}%"
    )

    st.progress(float(probability))

    st.subheader("Customer Summary")

    st.dataframe(input_df)