import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("final_cleaned_videodata.csv")

# Show first 5 rows
print(df.head())

# Show dataset structure
print(df.info())

# Show basic statistics
print(df.describe())

# -------------------------
# HOUR 2: DESCRIPTIVE STATS
# -------------------------

# Income distribution
print("\nIncome distribution:")
print(df["income"].value_counts())

# Percentage distribution
print("\nIncome percentage distribution:")
print(df["income"].value_counts(normalize=True) * 100)

# Average age by income
print("\nAverage age by income:")
print(df.groupby("income")["age"].mean())

# Average working hours by income
print("\nAverage working hours per week by income:")
print(df.groupby("income")["hours-per-week"].mean())

import matplotlib.pyplot as plt

# -------------------------
# HOUR 3: SIMPLE CHARTS
# -------------------------

# Histogram: Age distribution
plt.figure()
df["age"].hist(bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Bar chart: Income distribution
plt.figure()
df["income"].value_counts().plot(kind="bar")
plt.title("Income Distribution")
plt.xlabel("Income")
plt.ylabel("Count")
plt.show()

# Bar chart: Education distribution (top 10)
plt.figure()
df["education"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Education Levels")
plt.xlabel("Education")
plt.ylabel("Count")
plt.show() 