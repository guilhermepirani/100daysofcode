'''Sends a SMS warning if you should take an umbrella with you'''

import os
import requests
from twilio.rest import Client


# Wheater api variables https://openweathermap.org/api/one-call-api
WHEATER_API = 'https://api.openweathermap.org/data/2.5/onecall'
WHEATER_API_KEY = 'f005619efb70bce7bbf3ddad921cd47c' #Free
WHEATER_API_PARAMS = {
    'lat': -23.956289,
    'lon': -46.326462,
    'exclude': 'current,minutely,daily',
    'appid': WHEATER_API_KEY,
}

# SMS api variables from twilio free account https://www.twilio.com/docs/sms/quickstart/python
ACCOUNT_SID = 'AC2178cfc57c946bae63719804bebdfb72'
AUTH_TOKEN = '97ddebda7ed0bffa26145f0ad2dacfee'
API_PHONE = '+13107766729'


# Getting wheater for next 12 hours
response = requests.get(WHEATER_API, params=WHEATER_API_PARAMS)
response.raise_for_status()
weather_data = response.json()['hourly'][:12]

# Finds out if you may need an umbrella
umbrella = False
for hour_data in weather_data:
    code = hour_data['weather'][0]['id']
    if int(code) < 700: 
        umbrella = True

# Sending SMS if an umbrella is needed
if umbrella:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
                    .create(
                        body="Bring an umbrella!",
                        from_=API_PHONE,
                        to='ENTER PHONE WITH AUTH BY TWILIO ACCOUNT -> same format as from'
                    )

    print(message.status)
