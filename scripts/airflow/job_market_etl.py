from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="job_market_etl",
    start_date=datetime(2026, 1, 1),
    schedule="@hourly",
    catchup=False,
    tags=["etl", "jobs"],
) as dag:

    extract_jobs = BashOperator(
        task_id="extract_jobs",
        bash_command="cd /Users/natashamenon/Documents/job-market-etl && /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 scripts/extract_jobs.py",
    )

    transform_jobs = BashOperator(
        task_id="transform_jobs",
        bash_command="cd /Users/natashamenon/Documents/job-market-etl && /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 scripts/transform_jobs.py",
    )

    load_jobs = BashOperator(
        task_id="load_jobs",
        bash_command="cd /Users/natashamenon/Documents/job-market-etl && /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 scripts/load_jobs.py",
    )

    extract_jobs >> transform_jobs >> load_jobs