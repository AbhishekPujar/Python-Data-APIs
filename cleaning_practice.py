
import pandas as pd

# Load CSV dataset
df = pd.read_csv("data/sales.csv")

print("Original Dataset:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Convert date column into date format
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Remove rows with invalid dates
df = df.dropna(subset=["date"])

# Calculate revenue
df["revenue"] = df["quantity"] * df["unit_price"]

print("\nCleaned Dataset:")
print(df)

# Save cleaned data
df.to_csv("data/cleaned_sales.csv", index=False)

print("\nData cleaning completed!")
