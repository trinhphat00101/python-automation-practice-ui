import unittest
from unittest.mock import MagicMock, patch

from python_automation_practice_ui.page_object.ui_testing_playground.playground_main_page import PlaygroundMainPage
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestPlaygroundMainPage(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.page = PlaygroundMainPage(self.driver)

    @patch.object(WebDriver, "get")
    def test_open(self, patch_open):
        self.page.open()
        assert patch_open.called, "Open method not called"

    @patch.object(WebDriver, "find_element")
    def test_title_element(self, patch_f):
        self.page.title_element()
        assert patch_f.called, "Title element is not call correct method"

    @patch.object(WebDriver, "find_element")
    def test_block_quote_element(self, patch_f):
        self.page.block_quote_element()
        assert patch_f.called, "Block quote element is not call correct method"

    @patch.object(WebDriver, "find_element")
    def test_block_quote_alert_element(self, patch_f):
        self.page.block_quote_alert_element()
        assert patch_f.called, "Block quote alert element is not call correct method"

    @patch.object(WebDriver, "find_element")
    def test_description_element(self, patch_f):
        self.page.description_element()
        assert patch_f.called, "Description element is not call correct method"
