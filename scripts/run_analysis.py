import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# Paths

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed" / "cleaned_retail_sales.csv"
FIGURES_PATH = BASE_DIR / "outputs" / "figures"
SUMMARY_PATH = BASE_DIR / "outputs" / "summary"

FIGURES_PATH.mkdir(parents=True, exist_ok=True)
SUMMARY_PATH.mkdir(parents=True, exist_ok=True)


# Load Data

df = pd.read_csv(DATA_PATH)
df["date"] = pd.to_datetime(df["date"])


# KPIs

total_revenue = df["total_amount"].sum()
avg_transaction_value = df["total_amount"].mean()
total_transactions = len(df)
unique_customers = df["customer_id"].nunique()


# Save KPI Summary

summary_text = f"""
Retail Sales Analysis Summary

Total Revenue: {total_revenue:,.0f}
Average Transaction Value: {avg_transaction_value:,.2f}
Total Transactions: {total_transactions}
Unique Customers: {unique_customers}
"""

with open(SUMMARY_PATH / "kpi_summary.txt", "w") as f:
    f.write(summary_text)


# Monthly Revenue Trend

monthly_sales = (
    df.set_index("date")
      .resample("M")["total_amount"]
      .sum()
)

plt.figure(figsize=(7, 4))
monthly_sales.plot()
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig(FIGURES_PATH / "monthly_revenue_trend_auto.png")
plt.close()


# Revenue by Product Category

category_revenue = (
    df.groupby("product_category")["total_amount"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(6, 4))
category_revenue.plot(kind="bar")
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig(FIGURES_PATH / "revenue_by_category_auto.png")
plt.close()

print("Analysis completed successfully.")
