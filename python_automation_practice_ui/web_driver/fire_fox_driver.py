from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def init_firefox_driver():
    return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


class FirefoxDriver:
    def __init__(self):
        self.driver = init_firefox_driver()
