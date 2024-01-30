import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait


class BaseClass:
    driver = None
    # wait = None

    # @staticmethod
    def open_browser(self, browser_name):
        if browser_name == "chrome":
            service_obj = Service(os.getcwd().rsplit("\\", 1)[0] + "\\Drivers\\chromedriver.exe")
            self.driver = webdriver.Chrome(service=service_obj)
        elif browser_name == "edge":
            service_obj = Service(os.getcwd().rsplit("\\", 1)[0] + "\\Drivers\\msedgedriver.exe")
            self.driver = webdriver.Edge(service=service_obj)
        return self.driver

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        return WebDriverWait(self.driver, 60)
