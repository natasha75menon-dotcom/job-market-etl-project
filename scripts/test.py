import requests

APP_ID = "6ee8a605"
APP_KEY = "5aef01d993186d7d9cc57b3f6a092b26"

url = "https://api.adzuna.com/v1/api/jobs/gb/search/1"

params = {
    "app_id": APP_ID,
    "app_key": APP_KEY
}

response = requests.get(url, params=params)

print("Status Code:", response.status_code)
print("\nResponse:")
print(response.text[:500])
exit()
