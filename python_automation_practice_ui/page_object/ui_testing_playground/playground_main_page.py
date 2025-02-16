from python_automation_practice_ui.page_object.web_locator.playground_locator import PlayGroundUrl, PlayGroundId, \
    PlayGroundXpath
from python_automation_practice_ui.web_driver.web_driver import WebDriver
from selenium.webdriver.common.by import By


class PlaygroundMainPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(PlayGroundUrl.MAIN_PAGE.value)

    def title_element(self):
        return self.driver.find_element(By.ID, PlayGroundId.TITLE.value)

    def title_text(self):
        var = self.title_element().text
        return var

    def block_quote_element(self):
        return self.driver.find_element(By.XPATH, PlayGroundXpath.BLOCK_QUOTE.value)

    def block_quote_text(self):
        return self.block_quote_element().text

    def block_quote_footer_element(self):
        return self.driver.find_element(By.XPATH, PlayGroundXpath.BLOCK_QUOTE_FOOTER.value)

    def block_quote_footer_text(self):
        return self.block_quote_footer_element().text

    def block_quote_alert_element(self):
        return self.driver.find_element(By.XPATH, PlayGroundXpath.BLOCK_ALERT.value)

    def block_quote_alert_text(self):
        return self.block_quote_alert_element().text

    def description_element(self):
        return self.driver.find_element(By.XPATH, PlayGroundXpath.PAGE_DESCRIPTION.value)

    def description_text(self):
        return self.description_element().text


if __name__ == '__main__':
    dict_options = {
        "timeouts.pageLoad": 5000,
        "timeouts.implicit": 5000,
        "max_windows_size": True
    }
    driver = WebDriver("chrome", dict_options).driver
    page_playground = PlaygroundMainPage(driver)
    page_playground.open()
    print(page_playground.title_text())
    print(page_playground.block_quote_text())
    print(page_playground.block_quote_footer_text())
    print(page_playground.block_quote_alert_text())
    print(page_playground.description_text())
