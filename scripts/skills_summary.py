import pandas as pd

df = pd.read_csv("data/jobs_skills.csv")

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
summary = []

for skill in skills:
    summary.append({
        "skill": skill,
        "count": int(df[skill].sum())
    })

summary_df = pd.DataFrame(summary)

summary_df = summary_df.sort_values(
    by="count",
    ascending=False
)

summary_df.to_csv(
    "data/skills_summary.csv",
    index=False
)

print(summary_df)