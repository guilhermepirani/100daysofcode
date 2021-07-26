'''Sends a email to alert you the price of a product'''

import lxml
import requests
import smtplib
from bs4 import BeautifulSoup


DESIRED_PRICE = 2500.0
PRODUCT_URL = 'https://amzn.to/2UUUS6G'
HEADERS = {
    'Accept-Language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
}

# Email Credentials
EMAIL_ADDR = ''
EMAIL_PASSWORD = ''


# Get HTML from Amazon
response = requests.get('https://amzn.to/2UUUS6G', headers=HEADERS)
response.raise_for_status()
website_html = response.text

# Scrap for product's price
soup = BeautifulSoup(website_html, 'lxml')
price_tag = float(
    ''.join(
        soup.find(
            name="span", 
            id="priceblock_ourprice"
        ).getText().split()[1].replace(',', '.').split('.')[:2]
    )
)

# Send alert when price reaches desired value
if price_tag < DESIRED_PRICE:
        contents = f'A product has reached your desired price: {PRODUCT_URL}'
        connection = smtplib.SMTP('smtp.gmail.com', port=587)
        connection.starttls()
        connection.login(user=EMAIL_ADDR, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDR,
            to_addrs=EMAIL_ADDR,
            msg=f'Subject:PRICE ALERT\n\n{contents}'
        )
