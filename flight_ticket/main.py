#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import user
from datetime import datetime, timedelta

START_LOCATION = 'LON'


f = FlightSearch()
tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(days=180)
tomorrow.strftime("%d/%m/%Y")
six_months.strftime("%d/%m/%Y")


data = DataManager()
price = data.get_data()
#print(price)
for i in price:
    if i['iataCode'] == "":
        flight = f.flight(i['city'])['locations'][0]['code']
        i['iataCode'] = flight
        data.update_data(flight, i['id'])
    else:
        pass

    fly_rate = f.check_flight(
        START_LOCATION,
        i['iataCode'],
        tomorrow,
        six_months)

    #print(fly_rate)

    if fly_rate is None:
        continue

    if int(fly_rate) < i['lowestPrice']:
        EMAILS = user.get_user_mails()
        message = f"The flight rate from London to {i['city']} is now £{fly_rate}. This is soo good for you."
        link = f"https://www.google.co.uk/flights?hl=en#flt={i['city']}  to book your flight NOW!!!"

        send = NotificationManager()
        send.send_mails(EMAILS,message,link)


