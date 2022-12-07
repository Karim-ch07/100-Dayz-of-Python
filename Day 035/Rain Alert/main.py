import requests
from twilio.rest import Client

account_sid = "[ACCOUNT SID]"
auth_token = "[TOKEN]"

API_KEY = "[API KEY]"
OWM_WEATHER_EP = "https://api.openweathermap.org/data/2.5/weather?"
OWM_FORECAST_EP = "https://api.openweathermap.org/data/2.5/forecast?"
OWM_ONECALL_EP = "https://api.openweathermap.org/data/2.5/onecall?"

MY_LAT = 52.525578
MY_LNG = 13.373325

params_weather = {
    "q": "Poznan",
    "appid": API_KEY,
}

params_onecall = {
    "lat" : MY_LAT,
    "lon" : MY_LNG,
    # "exclude" : {part},
    "appid": API_KEY,
}

response = requests.get(OWM_WEATHER_EP, params=params_weather)
response.raise_for_status()

current_weather = response.json()["weather"]

will_rain = False
for weather in current_weather:
    if weather["id"] <= 700:
        pass
    will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is going to rain, take an umbrella!",
        from_="+SOURCE NO",
        to="+VERIFIED NO",
    )

print(message.status)
