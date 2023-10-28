from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By


class GuviInsta:

    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def ff_count(self):
        try:
            # get the url
            self.driver.get(self.url)
            self.driver.maximize_window()
            sleep(2)
            # close the window with login and signup button
            pop = self.driver.find_element(By.XPATH, "//*[contains(@class, 'abck _aa5t _abcm')]")
            if pop:
                self.driver.find_element(By.XPATH, "//*[contains(@class, 'abck _aa5t _abcm')]/button").click()
            # get the count of the followers
            print(self.driver.find_element(By.XPATH, "//*[contains(text(), 'followers')]").text)
            # get the count of the following
            print(self.driver.find_element(By.XPATH, "//*[contains(text(), 'following')]").text)
        except:
            print("An exception occurred")

    def shutdown(self):
        self.driver.close()


url = "https://www.instagram.com/guviofficial/"
# create object for the class
gi = GuviInsta(url)
# call the methods
gi.ff_count()
gi.shutdown()
