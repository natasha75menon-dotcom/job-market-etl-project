import pandas as pd
import os

df = pd.read_csv("data/jobs_raw.csv")

print("Rows before cleaning:", len(df))

columns_to_keep = [
    'title',
    'company',
    'location',
    'salary_min',
    'salary_max',
    'description'
]

df = df[columns_to_keep]

df = df.drop_duplicates()

print("Rows after cleaning:", len(df))

os.makedirs("data", exist_ok=True)

df.to_csv("data/jobs_clean.csv", index=False)
df["average_salary"] = (df["salary_min"] + df["salary_max"]) / 2
print("Cleaned data saved successfully!")