import requests
from bs4 import BeautifulSoup

MY_PRICE = 5000

website = "https://www.jumia.com.ng/generic-wood-office-table-office-table-laptop-desk-214167121.html"
response = requests.get(url=website)
page = response.text

soup = BeautifulSoup(page, 'html.parser')

span = soup.find_all('span', class_='-b -ltr -tal -fs24')
price = [price.getText().split(" ")[1] for price in span]

for p in price:
    rate = int(p.replace(',', ''))
    print(rate)
    if rate < MY_PRICE:
        print("Buy Now")
    else:
        print("Not yet")
