import requests
import datetime

GENDER = 'Male'
WEIGHT_KG = '60'
HEIGHT_CM = '100'
AGE = '22'

API_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
API_KEY = '8028e958fe49602abf6d215e50f0912b'
API_ID = 'b7b166aa'

SHEETY_API = 'https://api.sheety.co/f31713ee5ec8d8d97a39f5d301cdc14d/myWorkouts/workouts'


exercise_text = input("Tell me which exercises you did: ")

headers = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,

}

response = requests.post(API_ENDPOINT, headers=headers, json=parameters)
# response.raise_for_status()
data = response.json()
print(data)



###############################________________##########################

today = datetime.datetime.now()
time_now = datetime.datetime.now().strftime('%X')

for exercise in data["exercises"]:
    SHEETY_DETAILS = {
        "workout": {
            'date': today.strftime('%d/%m/%Y'),
            'time': time_now,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }
    response = requests.post(url=SHEETY_API, json=SHEETY_DETAILS)
    print(response.text)

