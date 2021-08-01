'''Automates data entry for a renting price research job at Zillow'''

import time
from selenium import webdriver

from data import get_property_data


CHROME_WEBDRIVER_PATH = 'YOUR CHROME DRIVER PATH'
PROPERTY_CHOICES = 'LINK TO ZILLOW SEARCH RESULTS PAGE'
FORM_URL = 'YOUR FORM URL'


# Bs4 only scraps some elements from html because of javascript loading
properties_data = get_property_data(PROPERTY_CHOICES)

# Initialize webdriver and start submitting
driver = webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH)

for n in properties_data.keys():
    driver.get(FORM_URL)

    time.sleep(2)
    address = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    address.send_keys(properties_data[n]['address'])
    price.send_keys(properties_data[n]['price'])
    link.send_keys(properties_data[n]['link'])
    submit_button.click()
