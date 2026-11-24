
# ==================================================
# PYTHON DATA & APIs
# Python Sales Data Analysis Application
# ==================================================

# STEP 1: IMPORT LIBRARIES

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests


# STEP 2: CREATE OUTPUT FOLDER

os.makedirs("outputs", exist_ok=True)

print("=" * 50)
print(" PYTHON DATA ANALYSIS APPLICATION")
print("=" * 50)


# STEP 3: LOAD DATASET

print("\nSTEP 1: Loading Dataset")

df = pd.read_csv("data/sales.csv")

print("Dataset Loaded Successfully!")
print(df.head())


# STEP 4: DATA CLEANING

print("\nSTEP 2: Data Cleaning")

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Convert date column
df["date"] = pd.to_datetime(
    df["date"], errors="coerce"
)

# Convert numeric columns
df["quantity"] = pd.to_numeric(
    df["quantity"], errors="coerce"
)

df["unit_price"] = pd.to_numeric(
    df["unit_price"], errors="coerce"
)

# Remove invalid values
df = df.dropna(
    subset=["date", "quantity", "unit_price"]
)

# Fill missing product and category names
df["product"] = df["product"].fillna("Unknown")
df["category"] = df["category"].fillna("Unknown")

# Calculate revenue
df["revenue"] = (
    df["quantity"] * df["unit_price"]
)

# Save cleaned dataset
df.to_csv(
    "outputs/cleaned_sales.csv",
    index=False
)

print("Data Cleaning Completed!")


# STEP 5: NUMPY ANALYSIS

print("\nSTEP 3: NumPy Analysis")

revenue = df["revenue"].to_numpy()

total_revenue = np.sum(revenue)
average_revenue = np.mean(revenue)
maximum_revenue = np.max(revenue)
minimum_revenue = np.min(revenue)

print("Total Revenue:", total_revenue)
print("Average Revenue:", average_revenue)
print("Maximum Revenue:", maximum_revenue)
print("Minimum Revenue:", minimum_revenue)


# STEP 6: PANDAS ANALYSIS

print("\nSTEP 4: Pandas Analysis")

# Total quantity sold
total_quantity = df["quantity"].sum()

# Product-wise sales
product_sales = df.groupby(
    "product"
)["quantity"].sum()

# Find best-selling product
best_product = product_sales.idxmax()

# Category-wise revenue
category_sales = df.groupby(
    "category"
)["revenue"].sum()

# Find highest revenue category
best_category = category_sales.idxmax()

# Daily sales
daily_sales = df.groupby(
    "date"
)["revenue"].sum()

print("Total Quantity Sold:", total_quantity)

print("Best-Selling Product:", best_product)

print("Highest Revenue Category:", best_category)

print("\nCategory-wise Revenue:")
print(category_sales)


# STEP 7: REST API INTEGRATION

print("\nSTEP 5: REST API Integration")

url = "https://jsonplaceholder.typicode.com/users"

try:

    response = requests.get(url, timeout=15)

    response.raise_for_status()

    api_data = response.json()

    # Convert JSON into DataFrame
    api_df = pd.json_normalize(api_data)

    # Save API information
    api_df.to_csv(
        "outputs/api_users.csv",
        index=False
    )

    print("API Connected Successfully!")

    print("\nAPI User Details:")
    print(api_df[["name", "email"]].head())

except requests.exceptions.RequestException as error:

    print("API Connection Error:", error)

except ValueError as error:

    print("JSON Processing Error:", error)


# STEP 8: DATA VISUALIZATION

print("\nSTEP 6: Creating Charts")

sns.set_theme(style="whitegrid")


# BAR CHART

plt.figure(figsize=(8, 5))

sns.barplot(
    x=category_sales.index,
    y=category_sales.values
)

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue (INR)")

plt.tight_layout()

plt.savefig("outputs/category_sales.png")

plt.close()


# LINE CHART

plt.figure(figsize=(10, 5))

plt.plot(
    daily_sales.index,
    daily_sales.values,
    marker="o"
)

plt.title("Daily Sales Revenue")
plt.xlabel("Date")
plt.ylabel("Revenue (INR)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("outputs/daily_sales.png")

plt.close()


# PIE CHART

plt.figure(figsize=(7, 7))

plt.pie(
    category_sales.values,
    labels=category_sales.index,
    autopct="%1.1f%%"
)

plt.title("Revenue Distribution")

plt.tight_layout()

plt.savefig("outputs/revenue_distribution.png")

plt.close()

print("All Charts Created Successfully!")


# STEP 9: GENERATE ANALYSIS REPORT

print("\nSTEP 7: Generating Report")

report = f"""
==========================================
       PYTHON DATA ANALYSIS REPORT
==========================================

Total Orders: {len(df)}

Total Quantity Sold: {total_quantity}

Total Revenue: Rs. {total_revenue:,.2f}

Average Revenue Per Order:
Rs. {average_revenue:,.2f}

Highest Order Revenue:
Rs. {maximum_revenue:,.2f}

Lowest Order Revenue:
Rs. {minimum_revenue:,.2f}

Best-Selling Product:
{best_product}

Highest Revenue Category:
{best_category}

------------------------------------------
CATEGORY-WISE REVENUE
------------------------------------------

{category_sales.to_string()}

------------------------------------------
DATASET STATISTICS
------------------------------------------

{df.describe().to_string()}

==========================================
          REPORT COMPLETED
==========================================
"""

with open(
    "outputs/analysis_report.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(report)


# STEP 10: FINAL MESSAGE

print("\n" + "=" * 50)
print("PROJECT COMPLETED SUCCESSFULLY!")
print("Check your outputs folder.")
print("=" * 50)
