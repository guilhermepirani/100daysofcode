'''Interacting with Pixela API using HTTP requests'''

import requests
from datetime import datetime

USERNAME = 'guilhermepirani'
TOKEN = 'mytokenstring'
GRAPH_ID = 'pagesread'
PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
HEADERS = {'X-USER-TOKEN': TOKEN}


# Creating user
'''
USER_PARAMS = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMS)
print(response.text)
'''

# Defining graph
'''
GRAPHS_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'
GRAPH_PARAMS = {
    'id': GRAPH_ID,
    'name': 'Book Pages Read Tracker',
    'unit': 'Pages',
    'type': 'int',
    'color': 'sora',
}
response = requests.post(url=GRAPHS_ENDPOINT, json=GRAPH_PARAMS, headers=HEADERS)
print(response.text)
'''

# Add pixel to graph
NEW_PIXEL_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}'

today = datetime.now()

PIXEL_PARAMS = {
    'date': today.strftime('%Y%m%d'), # yyyyMMdd
    'quantity': '3',
}

response = requests.post(url=NEW_PIXEL_ENDPOINT, json=PIXEL_PARAMS, headers=HEADERS)
print(response.text)

PIXEL_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}'

# Update a pixel
'''
UPDATE_PARAMS = {
    'quantity': '5',
}
response = requests.put(url=UPDATE_ENDPOINT, json=UPDATE_PARAMS, headers=HEADERS)
print(response.text)
'''

# Delete a pixel
'''
response = requests.delete(url=UPDATE_ENDPOINT, json=UPDATE_PARAMS, headers=HEADERS)
print(response.text)
'''