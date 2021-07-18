'''Using NPL and an API to interact with google sheets'''

import requests
from datetime import datetime


GENDER = '_MALE_OR_FEMALE_'
WEIGHT_KG = _YOUR_WEIGHT_INT
HEIGHT_CM = _YOUR_HEIGHT_INT
AGE = _YOUR_AGE_INT

# Nutritionix API provides a NPL service directed to exercising
NUTRI_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
NUTRI_HEADERS = {
    'x-app-id': '_YOUR_ID_',
    'x-app-key': '_YOUR_KEY_',
}

# Sheety API interacts with google sheets
SHEETY_ENDPOINT = 'https://api.sheety.co/<PATH_TO_YOUR_SHEET>'
SHEETY_HEADERS = {
    'Authorization': 'Bearer _YOUR_TOKEN_'
}


now = datetime.now()
today_date = now.strftime("%d/%m/%Y")
now_time = now.strftime("%X") # Hour

# User entry to parse with NPL API
query = input('Tell me which exercises you did: ')

nutri_params = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

nutri_response = requests.post(url=NUTRI_ENDPOINT, json=nutri_params, headers=NUTRI_HEADERS)
nutri_response.raise_for_status()
result = nutri_response.json()

# Gets return from Nutritionix and prepares input for Sheety
for exercise in result["exercises"]:
    sheety_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        },
    }

    # One API call for exercise
    sheety_response = requests.post(SHEETY_ENDPOINT, json=sheety_inputs, headers=SHEETY_HEADERS)

    print(sheety_response.text)