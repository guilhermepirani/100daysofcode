import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self) -> None:
        # Start speed test
        self.driver.get('https://www.speedtest.net/')
        time.sleep(5)
        self.driver.find_element_by_css_selector('.js-start-test').click()
        time.sleep(60)

        # Retrieve net speed data
        d = self.driver.find_element_by_css_selector('.download-speed').text
        u = self.driver.find_element_by_css_selector('.upload-speed').text

        # Assign data to attributes
        self.down = int(d.split('.')[0])
        self.up = int(u.split('.')[0])

    def tweet_at_provider(self, tname: str, tpass: str, contents:str) -> None:
        # Login to Twitter
        self.driver.get('https://twitter.com/login?lang=pt')
        time.sleep(2)

        name = self.driver.find_element_by_name('session[username_or_email]')
        pwd = self.driver.find_element_by_name('session[password]')

        name.send_keys(tname)      
        pwd.send_keys(tpass)

        pwd.send_keys(Keys.ENTER)
        time.sleep(2)

        # Send tweet
        text_class = '.public-DraftStyleDefault-ltr'
        text = self.driver.find_element_by_css_selector(text_class)
        text.send_keys(contents)

        tweet_btn = '''//*[@id="react-root"]/div/div/div[2]/main/div/div/div/\
        div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/\
        div[2]/div[3]/div/span/span'''
        self.driver.find_element_by_xpath(tweet_btn).click()
        time.sleep(2)

        self.driver.quit()