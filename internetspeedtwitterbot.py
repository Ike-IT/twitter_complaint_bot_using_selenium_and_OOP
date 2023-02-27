from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


SERVICE_OBJ = Service("\C:\Development\chromedriver_win32")
TWITTER_URL = "https://twitter.com/"
SPEED_TESTER_URL = "https://www.speedtest.net/"

""" D blocks of codes below prevents D browser 4rm closing automatically """
options = Options()
options.AddExcludedArgument("enable-automation")
options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(service=SERVICE_OBJ, options=options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_TESTER_URL)
        time.sleep(20)
        accept_button = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        accept_button.click()
        time.sleep(4)
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed")
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        print(self.down.text)
        print(self.up.text)

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)

        time.sleep(20)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a')
        login_button.click()
        time.sleep(5)

        email_field = self.driver.find_element(By.NAME, 'text')
        email_field.click()
        email_field.send_keys("lesspython48@gmail.com")

        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_button.click()
        time.sleep(5)

        verify_field = self.driver.find_element(By.NAME, 'text')
        verify_field.click()
        verify_field.send_keys("pythonbreeds")

        """ Make sure you come back here"""
        time.sleep(3)
        sec_next_button = self.driver.find_element(By.CLASS_NAME, "css-1dbjc4n")
        sec_next_button.click()

        time.sleep(5)
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.click()
        password_field.send_keys("X)i2Tahx%)!ES09OB")

        sec_login_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/div')
        sec_login_button.click()

