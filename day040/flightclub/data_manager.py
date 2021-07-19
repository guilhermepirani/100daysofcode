import requests


ENDPOINT = 'https://api.sheety.co/<_YOUR_GOOGLE_SHEET_>'
HEADERS = {'Authorization': 'Bearer _YOUR_TOKEN_'}


class DataManager:
    '''This class is responsible for talking to the Google Sheet.'''
    
    def __init__(self):
        self.destination_data = {}

    def get_data(self):
        '''Returns data from the Google Sheet'''

        response = requests.get(url=ENDPOINT, headers=HEADERS)
        self.destination_data = response.json()['prices']
        return self.destination_data

    def post_iata(self):
        '''Posts data to the Google Sheet'''

        for city in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': city['iataCode'],
                }
            }

            response = requests.put(url=f'{ENDPOINT}/{city["id"]}', json=new_data, headers=HEADERS)
            print(response.text)