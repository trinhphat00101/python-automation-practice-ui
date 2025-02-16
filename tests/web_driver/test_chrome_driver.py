import unittest

from python_automation_practice_ui.web_driver.chrome_driver import WebChromeDriver


class TestChromeDriver(unittest.TestCase):
    def test_init_chrome_options(self):
        """Test init_chrome_options"""
        dict_options = {
            "timeouts.pageLoad": 5000,
            "timeouts.implicit": 5000,
            "max_windows_size": True
        }
        chrome = WebChromeDriver(dict_options=dict_options)
        assert chrome.options.timeouts['implicit'] == 5000, "Implicit wait time not correct"
        assert chrome.options.timeouts['pageLoad'] == 5000, "Implicit wait time not correct"
        assert chrome.options._arguments == ['start-maximized']

    def test_init_chrome_driver(self):
        """Test init_chrome_driver"""
        dict_options = {
            "timeouts.pageLoad": 5000,
            "timeouts.implicit": 5000,
            "max_windows_size": True
        }
        chrome = WebChromeDriver(dict_options=dict_options)
        assert chrome.driver.caps['browserName'] == "chrome"
