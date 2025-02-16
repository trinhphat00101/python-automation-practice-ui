from python_automation_practice_ui.web_driver.chrome_driver import WebChromeDriver


class WebDriver:
    def __init__(self, name_browser: str, dict_options=None):
        if dict_options is None:
            dict_options = {}
        self.name_browser = name_browser
        self.dict_options = dict_options
        self.driver = self.init_web_driver()

    def init_web_driver(self):
        if self.name_browser == "chrome":
            driver = WebChromeDriver(dict_options=self.dict_options)
        return driver.driver
