import pandas as pd

# Load dataset
df = pd.read_csv("final_cleaned_videodata.csv")

# Clean income labels (THIS FIXES THE ERROR)
df["income"] = df["income"].str.strip()

# QUERY 1: Income distribution
print("QUERY 1: Income distribution")
print(df["income"].value_counts())
print()

# QUERY 2: Average age by income
print("QUERY 2: Average age by income")
print(df.groupby("income")["age"].mean())
print()

# QUERY 3: Average working hours per week by income
print("QUERY 3: Average working hours per week by income")
print(df.groupby("income")["hours-per-week"].mean())
print()

# QUERY 4: Education vs income (top 5 for >50K)
print("QUERY 4: Top education levels contributing to >50K income")
edu_income = pd.crosstab(df["education"], df["income"])
print(edu_income.sort_values(by=">50K", ascending=False).head(5))
print()

# QUERY 5: Gender vs income
print("QUERY 5: Gender vs income distribution")
print(pd.crosstab(df["sex"], df["income"]))