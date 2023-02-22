import requests
from twilio.rest import Client

API_URL = "https://api.openweathermap.org/data/3.0/onecall"
API_KEY = "d31d803a56b75e1f4ad258d7f5c50bc3"

SID = "ACf3e4c1d372e8c6c05ab32c78058c8786"
AUTH_KEY = "409c5ccbd64da7277ef5514908c6255d"

weather_params = {
    "lat": 8.478600,
    "lon": 4.536080,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url=API_URL, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

today_rain = False
today_cloud = False

for hour in weather_slice:
    weather_code = hour['weather'][0]['id']
    if int(weather_code) < 620:
        today_rain = True

    elif int(weather_code) >= 800:
        today_cloud = True

client = Client(SID, AUTH_KEY)

if today_rain:
    message = client.messages.create(
        messaging_service_sid='MGc83126d912dec812d6f38ce6ebbad881',
        body='Huh...Its gonna rain 🌧️ today, Make sure you go out with your umbrella☂️. You are great \
        DevHalfboyfriend.',
        to='+2349032340534'
    )
    print(message.status)
elif today_cloud:
    message = client.messages.create(
        messaging_service_sid='MGc83126d912dec812d6f38ce6ebbad881',
        body='A bright 🔆 and Clear☀️ day ahead. Enjoy Your Day DevOwoyemi.',
        to='+2349032340534'
    )
    print(message.status)






