#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
import requests
from datetime import datetime, timedelta

START_LOCATION = 'LON'


f = FlightSearch()
tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(days=180)
tomorrow.strftime("%d/%m/%Y")
six_months.strftime("%d/%m/%Y")


data = DataManager()
price = data.get_data()
for i in price:
    if i['iataCode'] == "":
        flight = f.flight(i['city'])['locations'][0]['code']
        i['iataCode'] = flight
        data.update_data(flight, i['id'])
    else:
        pass


for dt in price:
    cost = f.check_flight(START_LOCATION, dt['iataCode'], tomorrow, six_months)
    print(cost)