-- Customer Churn Analysis — SQL version
-- Load WA_Fn-UseC_-Telco-Customer-Churn.csv into a table called `telco_churn`
-- (e.g. via SQLite, PostgreSQL, or BigQuery — any will work for a portfolio piece)

-- 1. Overall churn rate
SELECT
  ROUND(AVG(CASE WHEN Churn = 'Yes' THEN 1.0 ELSE 0 END), 3) AS churn_rate
FROM telco_churn;

-- 2. Churn rate by contract type
SELECT
  Contract,
  COUNT(*) AS customers,
  ROUND(AVG(CASE WHEN Churn = 'Yes' THEN 1.0 ELSE 0 END), 3) AS churn_rate
FROM telco_churn
GROUP BY Contract
ORDER BY churn_rate DESC;

-- 3. Churn rate by tenure bucket
SELECT
  CASE
    WHEN tenure <= 6 THEN '0-6 months'
    WHEN tenure <= 12 THEN '6-12 months'
    WHEN tenure <= 24 THEN '1-2 years'
    ELSE '2+ years'
  END AS tenure_bucket,
  COUNT(*) AS customers,
  ROUND(AVG(CASE WHEN Churn = 'Yes' THEN 1.0 ELSE 0 END), 3) AS churn_rate
FROM telco_churn
GROUP BY tenure_bucket
ORDER BY churn_rate DESC;

-- 4. Churn rate by internet service type
SELECT
  InternetService,
  COUNT(*) AS customers,
  ROUND(AVG(CASE WHEN Churn = 'Yes' THEN 1.0 ELSE 0 END), 3) AS churn_rate
FROM telco_churn
GROUP BY InternetService
ORDER BY churn_rate DESC;

-- 5. Churn rate by tech support status
SELECT
  TechSupport,
  COUNT(*) AS customers,
  ROUND(AVG(CASE WHEN Churn = 'Yes' THEN 1.0 ELSE 0 END), 3) AS churn_rate
FROM telco_churn
GROUP BY TechSupport
ORDER BY churn_rate DESC;

-- 6. Average monthly charges: churned vs retained
SELECT
  Churn,
  ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges,
  COUNT(*) AS customers
FROM telco_churn
GROUP BY Churn;

-- 7. Churn rate by payment method
SELECT
  PaymentMethod,
  COUNT(*) AS customers,
  ROUND(AVG(CASE WHEN Churn = 'Yes' THEN 1.0 ELSE 0 END), 3) AS churn_rate
FROM telco_churn
GROUP BY PaymentMethod
ORDER BY churn_rate DESC;
