import datetime
import os

import requests as requests

NUTRITION_X_API_KEY = os.environ["NUTRITION_X_API_KEY"]
NUTRITION_X_APP_ID = os.environ["NUTRITION_X_APP_ID"]

GENDER = "male"
WEIGHT = "80"
HEIGHT = "173"
AGE = 36

nutrition_x_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": NUTRITION_X_APP_ID,
    "x-app-key": NUTRITION_X_API_KEY,
}

query = input("Tell me which exercises you did: ")

request_body = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

nutrition_x_response = requests.post(url=nutrition_x_exercise_endpoint, json=request_body, headers=headers)
nutrition_x_result = nutrition_x_response.json()
print(nutrition_x_response.text)

sheety_endpoint = os.environ["SHEETY_ENDPOINT"]

bearer_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
}

for exercise in nutrition_x_result["exercises"]:
    sheety_request_body = {
        "workout": {
            "date": datetime.datetime.now().strftime("%Y.%m.%d"),
            "time": datetime.datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_request_body, headers=bearer_headers)
    print(sheety_response.text)
