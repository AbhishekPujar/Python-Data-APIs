
import pandas as pd

# Create student data
data = {
    "Name": ["Abhi", "Rahul", "Priya", "Kiran"],
    "Marks": [85, 90, 75, 95],
    "Age": [20, 21, 19, 22]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display complete data
print("Student Data:")
print(df)

# Display first two rows
print("\nFirst Two Rows:")
print(df.head(2))

# Display information
print("\nData Information:")
print(df.info())

# Calculate average marks
print("\nAverage Marks:", df["Marks"].mean())

# Find highest marks
print("Highest Marks:", df["Marks"].max())

# Sort students by marks
print("\nSorted Student Data:")
print(df.sort_values(by="Marks", ascending=False))
