from selenium import webdriver

chrome_driver_path = 'C:/Development/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get('https://amzn.to/2UUUS6G')
# price = driver.find_element_by_id('priceblock_ourprice')
# print(price.text)

driver.get('https://python.org')

# search_bar = driver.find_element_by_name('q')
# print(search_bar.get_attribute('placeholder'))

# logo = driver.find_element_by_class_name('python-logo')
# print(logo.size)

# doc_link = driver.find_element_by_css_selector('.documentation-widget a')
# print(doc_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# Scraping the events calendar and turning it into a JSON like dict
dates = driver.find_elements_by_css_selector('.event-widget .menu time')
events = driver.find_elements_by_css_selector('.event-widget .menu a')

calendar = {
    index: {
        'date': date.get_attribute('datetime').split('T')[0], 
        'name': name.text
    }
    for index, date, name
    in zip(range(len(dates)), dates, events)
}

print(calendar)
driver.quit()