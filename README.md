# 📊 E-Commerce Sales & Customer Analytics

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458)
![SQL](https://img.shields.io/badge/SQL-Analytics-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B)
![License](https://img.shields.io/badge/License-MIT-green)

An end-to-end **data analytics portfolio project** that turns e-commerce order data into business insights around revenue, profitability, customer behavior, products, regions, and sales channels.

> **Dataset note:** This project uses synthetic data generated specifically for portfolio use. No real customer or company data is included.

---

## 🎯 Project Objective

The goal is to demonstrate how a data analyst can take raw transactional data and answer practical business questions using **Python, SQL, data visualization, and an interactive dashboard**.

### Business Questions

- How is revenue changing over time?
- Which categories generate the most revenue?
- Which regions generate the most profit?
- Which products are top performers?
- What is the average order value?
- What percentage of customers make repeat purchases?
- Which sales channels perform best?

---

## 📈 Executive Summary

| KPI | Result |
|---|---:|
| 💰 Total Revenue | **$3.92M** |
| 📦 Total Orders | **12,000** |
| 👥 Customers | **3,000** |
| 💵 Total Profit | **$1.25M** |
| 📊 Profit Margin | **31.9%** |
| 🛒 Average Order Value | **$326.49** |
| 🔁 Repeat Customer Rate | **80.8%** |

---

## 📸 Dashboard & Analysis Screenshots

### Revenue Trend

![Revenue Trend](/revenue_trend.png)

### Revenue by Category

![Revenue by Category](/category_revenue.png)

### Profit by Region

![Profit by Region](/regional_profit.png)

---

## 🔎 Key Insights

### 1. Revenue shows seasonality

Monthly revenue follows a noticeable seasonal pattern, with stronger performance toward the end of the year.

**Business implication:** inventory, marketing budgets, and promotional campaigns should be planned around seasonal demand.

### 2. Revenue and profitability are different

The category with the highest revenue is not automatically the category with the highest profit margin.

**Business implication:** management should evaluate both revenue and profitability when allocating marketing spend.

### 3. Customer retention matters

More than **80% of customers in the synthetic dataset have made at least two purchases**.

**Business implication:** retention and repeat-purchase campaigns could be an important growth lever.

### 4. Regional performance varies

Profit contribution differs across regions.

**Business implication:** sales targets and promotional strategies can be customized by region rather than using a one-size-fits-all approach.

---

## 🧰 Tech Stack

| Tool | Purpose |
|---|---|
| **Python** | Data analysis and transformation |
| **Pandas** | Data cleaning and aggregation |
| **NumPy** | Data generation and numerical analysis |
| **SQL** | Business queries and analytical thinking |
| **Matplotlib** | Static visualizations |
| **Plotly** | Interactive visualizations |
| **Streamlit** | Interactive dashboard |
| **Jupyter** | Exploratory analysis |
| **Git/GitHub** | Version control and portfolio presentation |

---

## 🗂️ Project Structure

```text
ecommerce-analytics-portfolio/
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   └── orders.csv
│
├── reports/
│   ├── kpis.csv
│   ├── monthly_performance.csv
│   ├── category_performance.csv
│   ├── region_performance.csv
│   ├── revenue_trend.png
│   ├── category_revenue.png
│   └── regional_profit.png
│
├── screenshots/
│   ├── revenue_trend.png
│   ├── category_revenue.png
│   └── regional_profit.png
│
├── sql/
│   ├── schema.sql
│   └── analysis_queries.sql
│
├── src/
│   └── analysis.py
│
├── dashboard.py
├── ecommerce_analysis.ipynb
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🧪 Analytical Workflow

### Step 1 — Data Preparation

The project combines three logical datasets:

- Customers
- Products
- Orders

Calculated metrics include:

- Revenue
- Cost
- Profit
- Profit margin
- Discount percentage
- Average order value

### Step 2 — Exploratory Data Analysis

The analysis examines:

- Monthly revenue
- Monthly profit
- Category performance
- Regional performance
- Product performance
- Customer repeat behavior
- Sales-channel performance

### Step 3 — SQL Analysis

The `sql/analysis_queries.sql` file contains queries for:

- Monthly revenue and profit
- Top products
- Repeat-customer rate
- Category profitability
- Channel performance

### Step 4 — Dashboard

The Streamlit dashboard allows users to filter the analysis by:

- Category
- Sales channel
- Region

It displays KPI cards, revenue trends, category performance, regional profitability, and top products.

---


### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ecommerce-analytics-portfolio
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the dashboard

```bash
streamlit run dashboard.py
```

The dashboard will open in your browser.

---


## 👨‍💻 About This Project

This project was created as a **data analytics portfolio project** to demonstrate practical skills in:

**Data Cleaning → SQL → Exploratory Analysis → Business Metrics → Visualization → Dashboard → Business Recommendations**





---

## 📄 License

This project is available under the MIT License.
