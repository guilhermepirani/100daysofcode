''' Plays Cookie Clicker'''

import time
from selenium import webdriver


# Setting up webdriver
chrome_driver_path = 'C:/Development/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

# Cookie and Store items
cookie = driver.find_element_by_id('cookie')
store = driver.find_elements_by_css_selector('#store div')
items_ids = [item.get_attribute('id') for item in store]

# Minutes the game should run
game_time = time.time() + 60*5

# Runs game
while time.time() < game_time:
    # Time to check store
    timeout = time.time() + 5

    while time.time() < timeout:
        cookie.click()

    # Retrieve store prices
    upgrades = driver.find_elements_by_css_selector('#store b')
    prices = [
        int(price.text.split('-')[1].strip().replace(',', ''))
        for price in upgrades if price.text != ''
    ]
    
    # Retrieve money
    money = driver.find_element_by_id('money').text
    if ',' in money:
        money = money.replace(',', '')
    money = int(money)
        
    # Filter affordable upgrades and buys the most expensive
    affordable_up = {
        key: value for (key, value)
        in zip(prices, items_ids) if money > key
    }
    driver.find_element_by_id(affordable_up[max(affordable_up)]).click()

print(driver.find_element_by_id("cps").text)
