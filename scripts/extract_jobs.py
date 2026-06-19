import requests
import pandas as pd

APP_ID = "6ee8a605"
APP_KEY = "2e17602ab0e7c9ed1fab954b985b6c1d"

all_jobs = []

for page in range(1, 7):  # 6 pages × 50 jobs = about 300 jobs

    url = f"https://api.adzuna.com/v1/api/jobs/gb/search/{page}"

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": "data analyst",
        "results_per_page": 50
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        for job in data["results"]:
            all_jobs.append({
                "title": job.get("title"),
                "company": job.get("company", {}).get("display_name"),
                "location": job.get("location", {}).get("display_name"),
                "salary_min": job.get("salary_min"),
                "salary_max": job.get("salary_max"),
                "description": job.get("description")
            })

        print(f"Page {page} downloaded")

df = pd.DataFrame(all_jobs)

print(f"Total jobs collected: {len(df)}")

df.to_csv("data/jobs_raw.csv", index=False)
response = requests.get(url, params=params)

print("Status Code:", response.status_code)
print(response.text[:500])
