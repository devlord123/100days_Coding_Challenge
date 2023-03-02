import requests
from pprint import pprint


class DataManager:

    def __init__(self):
        self.PRICES = {}
        self.get_data()

    def get_data(self):
        SHEETY_API = 'https://api.sheety.co/f31713ee5ec8d8d97a39f5d301cdc14d/flightDeals/prices'
        response = requests.get(url=SHEETY_API)
        # response.raise_for_status()
        data = response.json()
        self.PRICES = data['prices']
        return self.PRICES

    def update_data(self, code, id):

        params = {
            'price': {
                'iataCode': code,
                'id': id
            }
        }
        response = requests.put(url=f"https://api.sheety.co/f31713ee5ec8d8d97a39f5d301cdc14d/flightDeals/prices/{id}",
                                json=params)

        print(response.text)



