ETL Analysis for the Job Market in the UK.

 Project Overview

The project does this by creating an end-to-end ETL pipeline that analyzes more than 300 job postings for Data Analyst positions in the UK. The pipeline fetches job market data, cleans and transforms it using Python and Pandas, stores it in a PostgreSQL database and creates a Tableau dashboard to visualize some of the insights.

The aim of the project is to try and determine the hiring trends, salary distribution, best hiring companies, location of jobs with high demand, and the skills that are the most in demand in the job market for Data Analyst in the UK.

 Technologies Used

 Python
 Pandas
 PostgreSQL
 Tableau Public
 Git
 GitHub

 ETL Pipeline

 Extract

 Fetched the job postings from the selected job data source.
 Collected job titles, companies, locations, job salary, job descriptions and skills.

 Transform

 Removed duplicate records.
 Selected relevant columns.
 Cleaned and standardized job data.
 Processed skill-related information for analysis.

 Load

 Imported the cleaned data into PostgreSQL.
 Prepared the data for dashboard reporting and visualization.

 Project Structure


job-market-etl/
│
├── data/
├── scripts/
├── sql/
├── dashboard/
├── README.md
└── requirements.txt


 Dashboard Insights

The Tableau dashboard will give insights on:

 The best places to find Data Analyst jobs in the UK are as follows:
 Top hiring companies
 Salary distribution
 The top-paying Data Analyst jobs are the ones that pay the most.
 Most demanded skills

 Key Findings

 London offers the greatest number of Data Analyst jobs.
 ITOL Recruit is among the top hiring firms in the data set.
 Most salaries fall within the £40,000–£60,000 range.
 There are a number of positions that pay over £100,000.
 SQL is still one of the most sought-after skills for Data Analyst jobs.

 Future Improvements

 Use Apache Airflow to automate the ETL process.
 Combine a variety of job data sources.
 Update data in real-time.
 Design salary analytics predictive models.

 Author

Natasha Menon

Master's Student (Business Analytics and Data Science)
