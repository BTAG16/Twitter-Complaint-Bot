import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

PROMISED_DOWN = 85
PROMISED_UP = 90
TWITTER_EMAIL = os.environ["EMAIL"]
TWITTER_USERNAME = os.environ["USERNAME"]
TWITTER_PASSWORD = os.environ["PASSWORD"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
speedtest_URL = "https://www.speedtest.net/"
twitter_URL = "https://x.com/"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.get_internet_speed()
        time.sleep(2)
        self.driver.quit()

    def get_internet_speed(self):
        self.driver.get(speedtest_URL)

        cookies = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
        go = self.driver.find_element(By.CLASS_NAME, value="start-text")
        down = self.driver.find_element(By.CLASS_NAME, value="download-speed")
        up = self.driver.find_element(By.CLASS_NAME, value="upload-speed")

        time.sleep(2)
        cookies.click()
        time.sleep(3)
        go.click()
        time.sleep(45)

        if float(down.text) < PROMISED_DOWN or float(up.text) < PROMISED_UP:
            complaint = (f"Hey Internet Provider, why is my internet speed {down.text} down/{up.text} "
                         f"up when I pay for {PROMISED_DOWN} down/{PROMISED_UP} up?")
            self.tweet_at_provider(complaint)


    def tweet_at_provider(self, complaint):
        self.driver.get(twitter_URL)

        time.sleep(3)
        cookie = self.driver.find_element(By.XPATH,
                                          value='//*[@id="layers"]/div/div[1]/div/div/div/div[2]/button[1]/div')
        cookie.click()

        sign_in = self.driver.find_element(By.XPATH,
                                           value='//*[@id="react-root"]/div/div/div[2]/'
                                                 'main/div/div/div[1]/div[1]/div/div[3]/div[3]/a/div')
        sign_in.click()
        time.sleep(5)

        email_entry = self.driver.find_element(By.XPATH,
                                               value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                     'div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/'
                                                     'div/div[2]/div/input')
        email_entry.send_keys(TWITTER_EMAIL, Keys.ENTER)
        time.sleep(5)

        username_entry = self.driver.find_element(By.XPATH,
                                                  value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                        'div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/'
                                                        'div/div[2]/div/input')
        if username_entry:
            username_entry.send_keys(TWITTER_USERNAME, Keys.ENTER)

        time.sleep(5)
        password_entry = self.driver.find_element(By.XPATH,
                                                  value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                        'div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/'
                                                        'div/div[2]/div[1]/input')
        password_entry.send_keys(TWITTER_PASSWORD, Keys.ENTER)
        time.sleep(10)

        post = self.driver.find_element(By.XPATH,
                                        value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/'
                                              'div[3]/a/div')
        post.click()
        time.sleep(5)

        message = self.driver.find_element(By.XPATH,
                                           value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/'
                                                 'div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/'
                                                 'div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/'
                                                 'div[2]/div/div/div/div/span')
        message.send_keys(complaint)
        time.sleep(3)

        tweet = self.driver.find_element(By.XPATH,
                                         value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/'
                                               'div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/'
                                               'button[2]/div/span/span')
        tweet.click()
