import requests
import os
from datetime import datetime

headers = {
    "x-app-id": os.environ.get("APP_ID"),
    "x-app-key": os.environ.get("APP_KEY"),
    "Content-Type": "application/json"
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_data = {
    "query": str(input("Tell me what exercise you did: ")),
}

response = requests.post(url=exercise_endpoint, json=exercise_data, headers=headers)
exercise_data = response.json()["exercises"]
date_today = datetime.now().strftime('%d/%m/%Y')
time_today = datetime.now().strftime('%X')
spreadsheet_endpoint = os.environ.get("SHEET_ENDPOINT")

for data in exercise_data:
    exercises = {
        "workout": {
            "date": date_today,
            "time": time_today,
            "exercise": data['name'].title(),
            "duration": data['duration_min'],
            "calories": data['nf_calories']
        }

    }

    sheet_response = requests.post(url=spreadsheet_endpoint,json=exercises,auth=(os.environ.get("USERNAME"), os.environ.get("PASSWORD")))
    print(sheet_response.text)


