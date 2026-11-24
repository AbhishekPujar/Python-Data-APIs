
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("data/cleaned_sales.csv")

# Set chart style
sns.set_theme(style="whitegrid")

# Calculate category-wise revenue
category_sales = df.groupby("category")["revenue"].sum()

# 1. Bar chart
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
plt.show()

# 2. Line chart
df["date"] = pd.to_datetime(df["date"])

daily_sales = df.groupby("date")["revenue"].sum()

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
plt.show()

# 3. Pie chart
plt.figure(figsize=(7, 7))

plt.pie(
    category_sales.values,
    labels=category_sales.index,
    autopct="%1.1f%%"
)

plt.title("Revenue Distribution")
plt.savefig("outputs/revenue_distribution.png")
plt.show()

print("All charts created successfully!")
