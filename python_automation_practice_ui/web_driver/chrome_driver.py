from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class WebChromeDriver:
    def __init__(self, dict_options=None):
        if dict_options is None:
            dict_options = {}
        self.dict_options = dict_options
        self.options = self.init_chrome_options()
        self.driver = self.init_chrome_driver()

    def init_chrome_driver(self):
        return webdriver.Chrome(options=self.options, service=ChromeService(ChromeDriverManager().install()))

    def init_chrome_options(self):
        dict_timeouts = {}
        if len(self.dict_options) > 0:
            options = webdriver.ChromeOptions()
        for key, value in self.dict_options.items():
            if key == "timeouts.pageLoad":
                dict_timeouts["pageLoad"] = value
            if key == "timeouts.implicit":
                dict_timeouts["implicit"] = value
            if key == "max_windows_size" and value:
                options.add_argument("start-maximized")
        if len(dict_timeouts) > 1:
            options.timeouts = dict_timeouts
        return options
