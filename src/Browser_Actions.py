from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
import os


class GoogleImage:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def search_google_images(self, query):
        self.driver.get('https://images.google.com/')
        assert "Google" in self.driver.title
        elem = self.driver.find_element_by_id("lst-ib")
        elem.send_keys(query)
        elem.send_keys(Keys.RETURN)

    def save_image(self):
        elem = self.driver.find_element_by_xpath("//div[@id='rg_s']/div/a/img[@class='rg_i']")
        src = elem.get_attribute('src')
        urllib.urlretrieve(src, 'Album Art.jpg')

    def del_image(self):
        os.remove('Album Art.jpg')

    def closeup(self):
        self.driver.close()
