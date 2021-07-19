import requests

from flight_data import FlightData


ENDPOINT = 'https://tequila-api.kiwi.com'
HEADERS = {'apikey': '_YOUR_API_KEY_'}


class FlightSearch:
    '''This class is responsible for talking to the Flight Search API.'''
    
    def get_iata(self, city):
        '''Returns iata code for given city'''

        iata_endpoint = f'{ENDPOINT}/locations/query'
        query = {"term": city, "location_types": "city"}
        response = requests.get(url=iata_endpoint, headers=HEADERS, params=query)
        return response.json()['locations'][0]['code']

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        '''Check flights prices'''

        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "BRL"
        }

        response = requests.get(url=f"{ENDPOINT}/v2/search", headers=HEADERS, params=query)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: R${flight_data.price}")
        return flight_data