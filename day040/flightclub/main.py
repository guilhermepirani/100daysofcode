'''Flight deal finder'''

from datetime import datetime, timedelta

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


ORIGIN_IATA = 'SAO'


data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_data()

# Fill iataCode cell when it's empty
if sheet_data[0]['iataCode'] == '':
    for row in sheet_data:
        row['iataCode'] = flight_search.get_iata(row['city'])
    data_manager.destination_data = sheet_data
    data_manager.post_iata()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# Check prices for each destination in data
for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_IATA,
        destination['iataCode'],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight != None:
        if flight.price < destination['lowestPrice']:
            notification_manager.send_sms(
                message=f'Low price alert! Only R${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to '
                f'{flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.'
            )