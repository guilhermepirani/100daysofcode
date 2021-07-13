'''Send news alerts based on stock price variation'''

import requests
from twilio.rest import Client


STOCK = 'TSLA'
COMPANY_NAME = 'Tesla'

STOCK_URL = 'https://www.alphavantage.co/query'
STOCK_API_KEY = '_YOUR_API_KEY_'
STOCK_API_PARAMS = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY,
    'outputsize': 'compact',
}

NEWS_URL = 'https://newsapi.org/v2/everything'
NEWS_API_KEY = '_YOUR_API_KEY_'
NEWS_API_PARAMS = {
    'apiKey': NEWS_API_KEY,
    'qInTitle': COMPANY_NAME,
}

TWILIO_ACCOUNT_SID = '_YOUR_ACCOUNT_SID_'
TWILIO_AUTH_TOKEN = '_YOUR_AUTH_TOKEN_'
TWILIO_API_PHONE = '_YOUR_VIRTUAL_PHONE_'


# Reach stock api endpoint
stock_response = requests.get(STOCK_URL, params=STOCK_API_PARAMS)
stock_response.raise_for_status()

# Fetches closing prices from yesterday and the day before (Stored in 'Time Series (Daily)'/slice :2/'4. close', inside json response)
stock_prices = [float(price['4. close']) for price in [day for day in stock_response.json()['Time Series (Daily)'].values()][:2]]

# Difference between daily closing prices
difference = stock_prices[0] - stock_prices[1]
diff_percentage = round((abs(difference) / stock_prices[0]) * 100, 2)
up_down = None
if difference > 0:
    up_down = "+"
else:
    up_down = "-"

# Send alert
if diff_percentage > 3:
    
    # Reach news api endpoint
    news_response = requests.get(NEWS_URL, params=NEWS_API_PARAMS)
    news_response.raise_for_status()

    # Slicing for the top 3 articles in json response
    articles = news_response.json()['articles'][:3]
    contents = [f'{STOCK}: {up_down}{diff_percentage}% \nHeadline: {article["title"]}. \nRead on: {article["url"]}' for article in articles]

    # Create twilio client and send message
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for content in contents:
        message = client.messages \
                    .create(
                        body=content,
                        from_=TWILIO_API_PHONE,
                        to='_YOUR_AUTH_PHONE_'
                    )
    print(message.status)