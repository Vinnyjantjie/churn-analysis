"""
Customer Churn Analysis — Telco Dataset
Portfolio Project: "Reducing Customer Churn for a Subscription Business"

Dataset: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
Download the CSV as: WA_Fn-UseC_-Telco-Customer-Churn.csv
Place it in the same folder as this script.

Run with: pip install pandas matplotlib --break-system-packages
          python churn_analysis.py
"""

import pandas as pd

pd.set_option("display.max_columns", None)

# -------------------------------------------------------------------
# STEP 1: LOAD + INSPECT
# -------------------------------------------------------------------
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Shape:", df.shape)
print("\nColumn types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())
print("\nFirst rows:\n", df.head())

# -------------------------------------------------------------------
# STEP 2: CLEAN
# -------------------------------------------------------------------

# Known issue: TotalCharges is stored as text and has some blank strings
# (usually for customers with tenure = 0, i.e. brand new customers)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
print("\nRows with missing TotalCharges after conversion:", df["TotalCharges"].isnull().sum())

# These are new customers (tenure=0), so it makes sense TotalCharges is blank.
# Decision: fill with 0 rather than drop the rows — document this choice in your case study.
df["TotalCharges"] = df["TotalCharges"].fillna(0)

# Convert target variable to a clean binary flag (easier for grouping/modeling later)
df["Churned"] = df["Churn"].map({"Yes": 1, "No": 0})

# Create a tenure bucket — raw tenure in months is harder to read in a chart
def tenure_bucket(months):
    if months <= 6:
        return "0-6 months"
    elif months <= 12:
        return "6-12 months"
    elif months <= 24:
        return "1-2 years"
    else:
        return "2+ years"

df["TenureBucket"] = df["tenure"].apply(tenure_bucket)

# -------------------------------------------------------------------
# STEP 3: BUSINESS QUESTIONS
# -------------------------------------------------------------------

print("\n=== Overall churn rate ===")
print(df["Churned"].mean().round(3))

print("\n=== Churn rate by contract type ===")
print(df.groupby("Contract")["Churned"].mean().round(3).sort_values(ascending=False))

print("\n=== Churn rate by tenure bucket ===")
print(df.groupby("TenureBucket")["Churned"].mean().round(3).sort_values(ascending=False))

print("\n=== Churn rate by internet service type ===")
print(df.groupby("InternetService")["Churned"].mean().round(3).sort_values(ascending=False))

print("\n=== Churn rate by tech support ===")
print(df.groupby("TechSupport")["Churned"].mean().round(3).sort_values(ascending=False))

print("\n=== Average monthly charges: churned vs not ===")
print(df.groupby("Churned")["MonthlyCharges"].mean().round(2))

print("\n=== Churn rate by payment method ===")
print(df.groupby("PaymentMethod")["Churned"].mean().round(3).sort_values(ascending=False))

# -------------------------------------------------------------------
# STEP 4: EXPORT A CLEAN SUMMARY TABLE FOR YOUR DASHBOARD
# -------------------------------------------------------------------
# This is the file you'll actually connect to Tableau / Power BI
df.to_csv("telco_churn_cleaned.csv", index=False)
print("\nSaved cleaned file: telco_churn_cleaned.csv")
