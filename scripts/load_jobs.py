import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://localhost/job_market_db")

df = pd.read_csv("data/jobs_clean.csv")

df.to_sql(
    "jobs",
    engine,
    if_exists="replace",  # replace instead of append
    index=False
)

print(f"{len(df)} rows loaded successfully!")