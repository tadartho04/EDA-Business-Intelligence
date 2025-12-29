import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("final_cleaned_videodata.csv")

# -------------------------------
# VISUAL 1: Income distribution
# -------------------------------
df["income"].value_counts().plot(kind="bar")
plt.title("Income Distribution")
plt.xlabel("Income")
plt.ylabel("Count")
plt.show()

# --------------------------------
# VISUAL 2: Gender vs Income
# --------------------------------
pd.crosstab(df["sex"], df["income"]).plot(kind="bar")
plt.title("Gender vs Income")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.show()

# --------------------------------
# VISUAL 3: Average hours per week by income
# --------------------------------
df.groupby("income")["hours-per-week"].mean().plot(kind="bar")
plt.title("Average Working Hours per Week by Income")
plt.xlabel("Income")
plt.ylabel("Average Hours")
plt.xticks(rotation=0)
plt.show()