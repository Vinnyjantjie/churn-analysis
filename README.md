# Reducing Customer Churn for a Subscription Telecom Business

**Tools:** SQL · Python (pandas) · Power BI
**Dataset:** [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) — 7,043 customers

---

## The Business Problem

Subscription businesses live and die by retention. Acquiring a new customer typically costs far more than keeping an existing one. This analysis looks at a telecom company losing **26.5% of its customers annually** and asks two questions:

1. Which customers are most likely to churn?
2. What's actually driving them to leave?

The goal wasn't just to describe churn, but to identify specific, actionable levers the business could pull to reduce it.

## Approach

I worked with a dataset of 7,043 customers covering demographics, account details (tenure, contract type, monthly charges) and the services each customer had (internet type, tech support, streaming, etc.), along with whether they churned.

**Data cleaning:** `TotalCharges` was stored as text with 11 blank values, all belonging to brand new customers with zero tenure. I converted the field to numeric and filled those blanks with 0, since a customer with no completed billing cycle logically has no total charges yet.

**Analysis:** I used SQL and Python to segment churn rate across contract type, customer tenure, internet service type, tech support status, monthly charges and payment method looking for the segments where churn was most concentrated.

**Visualization:** Findings were built into an interactive Power BI dashboard so a non-technical stakeholder could see the key drivers of churn at a glance.

## Key Findings

### 1. Contract type is the single biggest driver of churn
Month-to-month customers churn at **42.7%**, compared to **11.3%** for one year contracts and just **2.8%** for two year contracts, a 15x gap between the extremes and Contract length is by far the strongest signal in the data.

### 2. Churn risk is concentrated in the first six months
New customers churn at **52.9%** in their first 6 months, dropping to **35.9%** by month 12 and just **14%** after two years. The company isn't primarily losing loyal long term customers, it's losing people before they're fully onboarded.

### 3. Missing tech support correlates strongly with churn
Customers without tech support churn at **41.6%**, versus **15.2%** for those who have it. Fiber optic customers also churn substantially more than DSL customers (**41.9%** vs **19%**), suggesting service experience not just price plays a meaningful role.

**A notable outlier:** customers paying by electronic check churn at **45.3%**, dramatically higher than any other payment method (15–19%). The dataset doesn't explain why it's flagged here as a strong candidate for follow up research rather than an overclaimed conclusion.

## Recommendations

1. **Incentivize longer contracts.** Offer a modest discount or added perk for switching from month-to-month to annual plans, targeted at customers still in their first six months where both churn risk and conversion opportunity are highest.
2. **Build a structured onboarding program.** A proactive check-in process in the first 90 days (usage tips, a support call, a milestone email) could meaningfully reduce the steep early tenure drop off.
3. **Bundle tech support into standard packages,** especially for fiber customers, rather than treating it as a paid add-on. This is a low cost lever tied directly to one of the strongest churn signals in the data.
4. **Investigate the electronic check segment further.** The size of the gap suggests something specific friction in the payment experience or a demographic skew worth a closer look before designing a fix.

## Reflection

The most useful part of this analysis wasn't finding *that* churn was high, It was identifying *which* levers the business could realistically pull. Contract length and onboarding timing stood out as the two most actionable areas, because they're within the company's direct control, unlike broader factors like price sensitivity.

---

## What's in this repo

| File | Description |
|---|---|
| `churn_analysis.py` | Python (pandas) data cleaning and exploration |
| `churn_analysis_queries.sql` | The same analysis written in SQL |
| `telco_churn_cleaned.csv` | Cleaned dataset, ready for BI tools |

## Contact

**Vinny Shongwe** — Data Analyst
📧 [Vinnyjantjie@gmail.com](mailto:Vinnyjantjie@gmail.com) · 🔗 [LinkedIn](https://www.linkedin.com/in/vinny-shongwe-993732127/) · 🌐 [Portfolio](https://vinnyjantjie.github.io)
