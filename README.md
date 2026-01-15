# Retail Sales Data Analysis

## Overview
This project performs an end-to-end analysis of retail sales data to uncover customer behavior patterns, revenue drivers, and product performance insights. The objective is to demonstrate a structured data analysis workflow and derive business-oriented insights using Python.

## Business Questions
- Which customer segments generate the most revenue?
- How does spending behavior differ by gender and age?
- Which product categories drive the highest sales?
- Who are the most valuable customers?

## Dataset
- Source: Kaggle – Retail Sales Dataset
- Size: 1,000 transactions
- Key features:
  - Transaction date
  - Customer demographics (gender, age)
  - Product category
  - Quantity, price, and total transaction value

## Project Structure
Retail-sales-data-analysis/
├── data/
│ ├── raw/ # Original dataset
│ └── processed/ # Cleaned dataset
├── notebooks/
│ ├── 01_data_cleaning.ipynb
│ ├── 02_exploratory_data_analysis.ipynb
│ └── 03_customer_and_product_insights.ipynb
├── outputs/
│ ├── figures/ # Saved visualizations
│ └── summary/
├── requirements.txt
└── README.md


## Analysis Workflow
1. Data cleaning and validation
2. Exploratory data analysis (EDA)
3. Customer segmentation
4. Product performance analysis
5. Insight generation and visualization

## Key Insights
- Customers aged 30–49 contribute the highest share of revenue.
- Average transaction value varies by gender, indicating different purchasing behavior.
- A small group of customers accounts for a disproportionate amount of total revenue.
- Certain product categories consistently outperform others.

## Tools & Technologies
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Jupyter Notebook
- Git & GitHub

## How to Run
```bash
pip install -r requirements.txt
