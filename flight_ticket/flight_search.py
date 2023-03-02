import requests
from flight_data import FlightData
import pprint


TEQUILA_API = 'https://tequila-api.kiwi.com'
TOKEN = 'g84nv0xnbMhO1QHMi0zaLmgBQyiZ4pLO'

class FlightSearch:

    #This class is responsible for talking to the Flight Search API.
    def flight(self, city):
        location = f"{TEQUILA_API}/locations/query"
        head = {'apikey': TOKEN}
        search = {'term':city, "location_types": "city"}

        response = requests.get(url=location, headers=head, params=search)
        self.message = response.json()
        #print(self.message)
        return self.message


    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        header = {'apikey': TOKEN}
        search = {
            'fly_from': origin_city_code,
            'fly_to': destination_city_code,
            'date_from': from_time.strftime("%d/%m/%Y"),
            'date_to': to_time.strftime("%d/%m/%Y"),
            "curr": "GBP",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
        }

        response = requests.get(url=f'{TEQUILA_API}/v2/search', headers=header, params=search)

        try:
            data = response.json()['data'][0]

        except IndexError:
            raise IndexError(f'No flight for {destination_city_code}')
        else:
            return f"{data['cityTo']}: £{data['price']}"




# today = datetime.datetime.now().strftime("%d/%m/%Y")
# # print(today)
#
# f = FlightSearch()
# data = f.check_flight("LON", "PAR", today, '23/3/2023')
# print(data)


# for dt in data['data']:
#
#     print(f"{dt['cityTo']}: ${dt['price']}")