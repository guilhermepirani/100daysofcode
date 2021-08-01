import requests
from bs4 import BeautifulSoup


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7',
}

def get_property_data(url: str,) -> dict:
    '''Returns a dict of property, price, link for a given URL'''

    # Get HTML from URL
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get properties Addresses, prices and links
    addresses = [
        address.getText() for address 
        in soup.find_all(name='address', class_='list-card-addr')
    ]
    prices = [
        price.getText().split()[0] for price 
        in soup.find_all(name='div', class_='list-card-price')
    ]
    links = [
        link['href'] 
        if 'https' in link['href'] 
        else f'https://www.zillow.com/homedetails/{link["href"]}'
        for link 
        in soup.find_all(name='a', class_='list-card-link', href=True)
    ]

    # Organize data in JSON format dict
    properties_data = {
        key: {
            'address': address, 
            'price': price, 
            'link': link,
        }
        for (key, address, price, link)
        in zip(range(len(prices)), addresses, prices, links)
    }

    return properties_data