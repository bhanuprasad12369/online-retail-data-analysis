# 🛒 Online Retail Data Analysis

A beginner-level data analysis project using real-world online retail transaction data.

## 📌 Project Overview

This project analyzes online retail transaction data to understand sales performance, revenue trends, customer behavior, products, and country-wise sales.

The project uses Python and Pandas for data cleaning and analysis, and Matplotlib for visualization.

## 📊 Dataset

**Dataset:** UCI Online Retail Dataset

The dataset contains real-world online retail transaction data from 2010–2011.

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib
* UCI Machine Learning Repository
* Git & GitHub

## 🧹 Data Cleaning

The following steps were performed:

* Checked missing values
* Removed rows with missing product descriptions
* Removed duplicate rows
* Converted `InvoiceDate` to datetime format
* Identified negative quantities as returns/cancellations
* Removed non-positive quantities from sales analysis
* Removed non-positive unit prices from sales analysis
* Created a `TotalAmount` column

## 📈 Analysis Performed

* Total revenue analysis
* Monthly revenue analysis
* Country-wise revenue analysis
* Top products by revenue
* Customer-wise revenue analysis
* Monthly revenue visualization

## 💡 Key Business Insights

| Metric                    |         Result |
| ------------------------- | -------------: |
| Total Revenue             | £10,636,228.14 |
| Sales Rows After Cleaning |        524,231 |
| Highest Revenue Country   | United Kingdom |
| Highest Revenue Month     |  November 2011 |
| Top Customer ID           |          14646 |
| Top Customer Revenue      |    £280,206.02 |

## 📁 Project Files

```text
online_retail_analysis/
│
├── online_retail_analysis.py
├── cleaned_online_retail.csv
└── README.md
```

### `online_retail_analysis.py`

Python script containing the complete data cleaning, analysis, calculations, and visualization code.

### `cleaned_online_retail.csv`

Cleaned sales dataset generated from the analysis process.

### `README.md`

Project documentation and key results.

## 📊 Project Workflow

```text
Real Dataset
     ↓
Data Understanding
     ↓
Data Cleaning
     ↓
Data Transformation
     ↓
Revenue Analysis
     ↓
Customer & Product Analysis
     ↓
Visualization
     ↓
Business Insights
     ↓
GitHub
```

## 🎯 Conclusion

This project demonstrates a complete beginner-level data analysis workflow using real-world data.

It shows how Python and Pandas can be used to clean data, calculate business metrics, analyze trends, and generate useful business insights.

## 👨‍💻 Author

**Bhanu Satya Prasad Reddy**

Aspiring Data Engineer
