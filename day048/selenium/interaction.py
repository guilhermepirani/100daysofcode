from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Creating driver object
chrome_driver_path = 'C:/Development/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Opening website
# driver.get('https://en.wikipedia.org/wiki/Main_Page')

# Click on article count
# driver.find_element_by_css_selector('#articlecount a').click()

# Click on links without inspecting html
# driver.find_element_by_link_text('All portals').click()

# Interacting with the search bar
# search_bar = driver.find_element_by_name('search')
# search_bar.send_keys('Python', Keys.ENTER)

# Filling and submitting a form
driver.get('http://secure-retreat-92358.herokuapp.com/')

driver.find_element_by_name('fName').send_keys('Guilherme')
driver.find_element_by_name('lName').send_keys('Pirani')
driver.find_element_by_name('email').send_keys('emailthatiusefortests@gmail.com')
driver.find_element_by_xpath('/html/body/form/button').click()