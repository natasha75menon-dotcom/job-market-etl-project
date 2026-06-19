import pandas as pd

df = pd.read_csv("data/jobs_raw.csv")

skills = [
    "excel",
    "sql",
    "power bi",
    "tableau",
    "python",
    "statistics",
    "data analysis",
    "data analytics",
    "reporting",
    "visualization",
    "dashboard",
    "etl",
    "business intelligence"
]

for skill in skills:
    df[skill] = (
        df["description"]
        .fillna("")
        .str.lower()
        .str.contains(skill)
        .astype(int)
    )

df.to_csv("data/jobs_skills.csv", index=False)

print("Skills extracted successfully!")