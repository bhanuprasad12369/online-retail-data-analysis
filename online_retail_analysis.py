import pandas as pd
import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo

# Fetch Online Retail dataset
online_retail = fetch_ucirepo(id=352)

# Get the data
X = online_retail.data.features
y = online_retail.data.targets

print("Number of rows and columns:")
print(X.shape)

print("\nColumn names:")
print(X.columns)

print("\nData types:")
print(X.dtypes)

print("\nMissing values:")
print(X.isnull().sum())

print("\nMissing values percentage:")
print((X.isnull().sum() / len(X)) * 100)

print("\nDuplicate rows:")
print(X.duplicated().sum())

print("\nQuantity statistics:")
print(X["Quantity"].describe())

print("\nNegative Quantity rows:")
print((X["Quantity"] < 0).sum())

print("\nZero Quantity rows:")
print((X["Quantity"] == 0).sum())

print("\nPositive Quantity rows:")
print((X["Quantity"] > 0).sum())

print("\nUnitPrice statistics:")
print(X["UnitPrice"].describe())

print("\nZero UnitPrice rows:")
print((X["UnitPrice"] == 0).sum())

print("\nNegative UnitPrice rows:")
print((X["UnitPrice"] < 0).sum())

print("\nInvoiceDate sample:")
print(X["InvoiceDate"].head())

print("\nInvoiceDate data type:")
print(X["InvoiceDate"].dtype)

# Convert InvoiceDate to datetime
X = X.copy()
X["InvoiceDate"] = pd.to_datetime(X["InvoiceDate"])

print("\nInvoiceDate after conversion:")
print(X["InvoiceDate"].head())

print("\nNew InvoiceDate data type:")
print(X["InvoiceDate"].dtype)

print("\nCustomerID unique values:")
print(X["CustomerID"].nunique())

print("\nCustomerID missing values:")
print(X["CustomerID"].isnull().sum())

print("\nMissing Description rows:")
print(X["Description"].isnull().sum())

print("\nDescription sample:")
print(X["Description"].dropna().head(10))

# Remove rows with missing Description
X = X.dropna(subset=["Description"])

print("\nRows after removing missing Description:")
print(X.shape)

print("\nMissing Description after cleaning:")
print(X["Description"].isnull().sum())

# Remove duplicate rows
X = X.drop_duplicates()

print("\nRows after removing duplicates:")
print(X.shape)

print("\nDuplicate rows after cleaning:")
print(X.duplicated().sum())

print("\nNegative Quantity examples:")
print(X[X["Quantity"] < 0][["Description", "Quantity", "UnitPrice", "InvoiceDate"]].head(10))



# Create final sales dataframe
sales_df = X[
    (X["Quantity"] > 0) &
    (X["UnitPrice"] > 0)
].copy()

print("\nFinal sales dataframe shape:")
print(sales_df.shape)

print("\nQuantity <= 0 in sales_df:")
print((sales_df["Quantity"] <= 0).sum())

print("\nUnitPrice <= 0 in sales_df:")
print((sales_df["UnitPrice"] <= 0).sum())

# Calculate total sales amount
sales_df["TotalAmount"] = sales_df["Quantity"] * sales_df["UnitPrice"]

print("\nSales data with TotalAmount:")
print(sales_df[["Description", "Quantity", "UnitPrice", "TotalAmount"]].head(10))

# Calculate total revenue
total_revenue = sales_df["TotalAmount"].sum()

print("\nTotal Revenue:")
print(total_revenue)

# Create Year and Month columns
sales_df["Year"] = sales_df["InvoiceDate"].dt.year
sales_df["Month"] = sales_df["InvoiceDate"].dt.month

print("\nYear and Month:")
print(sales_df[["InvoiceDate", "Year", "Month"]].head(10))

# Monthly revenue analysis
monthly_sales = sales_df.groupby(["Year", "Month"])["TotalAmount"].sum().reset_index()

print("\nMonthly Revenue:")
print(monthly_sales)

# Country-wise revenue analysis
country_sales = sales_df.groupby("Country")["TotalAmount"].sum().reset_index()

country_sales = country_sales.sort_values(
    by="TotalAmount",
    ascending=False
)

print("\nCountry-wise Revenue:")
print(country_sales.head(10))

# Country-wise Revenue Chart

country_revenue = (
    sales_df.groupby("Country")["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))

country_revenue.plot(kind="bar")

plt.title("Top 10 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("country_revenue.png")

plt.show()

# Top products by revenue
product_sales = sales_df.groupby("Description")["TotalAmount"].sum().reset_index()

product_sales = product_sales.sort_values(
    by="TotalAmount",
    ascending=False
)

print("\nTop 10 Products by Revenue:")
print(product_sales.head(10))

# Top 10 Products Revenue Chart

top_products = product_sales.head(10)

plt.figure(figsize=(10, 6))

plt.bar(
    top_products["Description"],
    top_products["TotalAmount"]
)

plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=75)

plt.tight_layout()

plt.savefig("top_products_revenue.png")

plt.show()

# Customer-wise revenue analysis
customer_sales = sales_df.dropna(subset=["CustomerID"])

customer_sales = customer_sales.groupby("CustomerID")["TotalAmount"].sum().reset_index()

customer_sales = customer_sales.sort_values(
    by="TotalAmount",
    ascending=False
)

print("\nTop 10 Customers by Revenue:")
print(customer_sales.head(10))

# Top 10 Customers Revenue Chart

top_customers = customer_sales.head(10)

plt.figure(figsize=(10, 6))

plt.bar(
    top_customers["CustomerID"].astype(str),
    top_customers["TotalAmount"]
)

plt.title("Top 10 Customers by Revenue")
plt.xlabel("Customer ID")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("top_customers_revenue.png")

plt.show()


# Monthly revenue chart
plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales["Month"].astype(str),
    monthly_sales["TotalAmount"],
    marker="o"
)

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("monthly_revenue.png")
plt.show()

# Export cleaned sales dataset
sales_df.to_csv("cleaned_online_retail.csv", index=False)

print("\nCleaned dataset exported successfully!")

# Final project summary
print("\n================ PROJECT SUMMARY ================")

print("Total Revenue: £", round(total_revenue, 2))
print("Total Sales Rows:", len(sales_df))
print("Highest Revenue Country:", country_sales.iloc[0]["Country"])
print("Highest Revenue Month: November 2011")
print("Top Customer ID:", int(customer_sales.iloc[0]["CustomerID"]))
print("Top Customer Revenue: £", round(customer_sales.iloc[0]["TotalAmount"], 2))

print("=================================================")