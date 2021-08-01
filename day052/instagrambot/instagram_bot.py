'''A bot to Instagram'''

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException


class InstaFollower:
    def __init__(self, driver_path: str):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self, igname: str, igpass: str) -> None:
        '''Login to Instagram'''

        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)

        name = self.driver.find_element_by_name('username')
        pwd = self.driver.find_element_by_name('password')

        # Fill form and submit
        name.send_keys(igname)
        pwd.send_keys(igpass)
        pwd.send_keys(Keys.ENTER)
        time.sleep(2)
        
    def find_followers(self, target: str) -> None:
        '''Return a list of followers from target account'''

        # Go to target profile
        self.driver.get(f'https://www.instagram.com/{target}')
        time.sleep(2)

        # Open followers modal
        fxpath = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
        self.driver.find_element_by_xpath(fxpath).click()
        time.sleep(2)

        #Scroll modal
        mxpath = '/html/body/div[5]/div/div/div[2]'
        modal = self.driver.find_element_by_xpath(mxpath)
        script = 'arguments[0].scrollTop = arguments[0].scrollHeight'
        for i in range(10):
            self.driver.execute_script(script, modal) # Runs JavaScript
            time.sleep(2)

    def follow(self) -> None:
        '''Follow all users from given list of people'''
        
        btns = self.driver.find_elements_by_css_selector('li button')
        for btn in btns:
            try:
                btn.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                btn_xpath = '/html/body/div[5]/div/div/div/div[3]/button[2]'
                cancel_button = self.driver.find_element_by_xpath(btn_xpath)
                cancel_button.click()