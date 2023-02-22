from twilio.rest import Client
import requests


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_KEY = "B4R7FGFRIA1PD8EG"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = '1c5a322ed48b46e39bae5f45f649dffb'

SID = "ACf3e4c1d372e8c6c05ab32c78058c8786"
AUTH_KEY = "7d92f1be9cb1a758dbba553321ea3243"


stock_param={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_KEY
}
NEWS_PARAM = {
    "apiKey": NEWS_API,
    "qInTitle": COMPANY_NAME
}

response = requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo")
response.raise_for_status()
STOCK_DATA = response.json()


yesterday_closing = STOCK_DATA['Time Series (Daily)']['2023-02-21']['4. close']
bf_yesterday = STOCK_DATA['Time Series (Daily)']['2023-02-17']['4. close']
difference = abs(float(yesterday_closing) - float(bf_yesterday))
diff_percentage = (difference/ float(yesterday_closing)) * 100

up_down = None

if difference > 0:
    up_down = '🔺'
else:
    up_down = '🔻'


if abs(diff_percentage) > 1:
    news_api = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAM)
    news_api.raise_for_status()
    NEWS = news_api.json()
    articles = NEWS['articles']
    three_news = articles[:3]

    news_body = [f"{STOCK_NAME}: {up_down}{diff_percentage} \nHeadline: {article['title']}. \nBrief: {article['description']}" \
                 for article in three_news]
    client = Client(SID, AUTH_KEY)

    for item in news_body:
        message = client.messages.create(
            messaging_service_sid='MGc83126d912dec812d6f38ce6ebbad881',
            body=item,
            to='+2349032340534'
        )
        print(message.status)





