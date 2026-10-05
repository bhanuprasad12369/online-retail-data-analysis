# Online Retail Data Analysis

## Project Overview

This project analyzes real-world online retail sales data using Python and Pandas.

The goal is to understand sales performance, customer behavior, product revenue, and country-wise revenue.

## Dataset

Dataset: UCI Online Retail Dataset

The dataset contains online retail transaction data from 2010 to 2011.

## Technologies Used

* Python
* Pandas
* Matplotlib
* UCI Machine Learning Repository

## Data Cleaning

The following data cleaning steps were performed:

* Checked missing values
* Removed rows with missing product descriptions
* Removed duplicate rows
* Converted InvoiceDate to datetime format
* Identified negative quantities as returns/cancellations
* Removed non-positive quantities for sales analysis
* Removed non-positive unit prices for sales analysis

## Analysis Performed

* Total revenue calculation
* Monthly revenue analysis
* Country-wise revenue analysis
* Top products by revenue
* Customer-wise revenue analysis
* Monthly revenue visualization

## Key Results

* Total Revenue: £10,636,228.14
* Sales Rows After Cleaning: 524,231
* Highest Revenue Country: United Kingdom
* Highest Revenue Month: November 2011
* Top Customer ID: 14646
* Top Customer Revenue: £280,206.02

## Project Files

* `online_retail_analysis.py` — Python analysis code
* `cleaned_online_retail.csv` — Cleaned sales dataset
* `README.md` — Project documentation

## Conclusion

This project demonstrates how Python and Pandas can be used to clean, analyze, and visualize real-world retail data and generate useful business insights.
