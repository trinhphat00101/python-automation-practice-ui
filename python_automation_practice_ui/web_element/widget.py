from python_automation_practice_ui.web_driver.web_driver import WebDriver
from selenium.webdriver.common.by import By


class Widget:
    def __init__(self, driver, element_type, element_locator):
        self.driver = driver
        self.element_type = element_type
        self.element_locator = element_locator
        self.by = self.get_element_type()

    def get_element_type(self):
        res = By.ID
        if self.element_type == "XPATH":
            res = By.XPATH
        elif self.element_type == "NAME":
            res = By.NAME
        elif self.element_type == "LINK_TEXT":
            res = By.LINK_TEXT
        elif self.element_type == "PARTIAL_LINK_TEXT":
            res = By.PARTIAL_LINK_TEXT
        elif self.element_type == "TAG_NAME":
            res = By.TAG_NAME
        elif self.element_type == "CLASS_NAME":
            res = By.CLASS_NAME
        elif self.element_type == "CSS_SELECTOR":
            res = By.CSS_SELECTOR
        return res

    def get_element(self):
        return self.driver.find_element(self.by, self.element_locator)

    def get_elements(self):
        return self.driver.find_elements(self.by, self.element_locator)
