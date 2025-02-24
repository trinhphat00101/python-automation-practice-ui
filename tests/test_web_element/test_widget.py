import unittest
from unittest.mock import MagicMock, patch

from python_automation_practice_ui.page_object.web_locator.playground_locator import PlayGroundXpath
from python_automation_practice_ui.web_element.widget import Widget


class TestWidge(unittest.TestCase):
    def setUp(self) -> None:
        self.dict_options = {
            "start-maximized": True,
            "pageLoad": 2560,
            "implicit": 1440,
        }
        self.driver = MagicMock()
        self.element_locator = PlayGroundXpath.BLOCK_ALERT.value

    def test_get_element_type_xpath(self):
        widget = Widget(self.driver, element_type="XPATH", element_locator=self.element_locator)
        assert widget.by == "xpath", "Element type xpath not correct"

    def test_get_element_type_id(self):
        widget = Widget(self.driver, element_type="ID", element_locator=self.element_locator)
        assert widget.by == "id", "Element type id not correct"

    def test_get_element_type_name(self):
        widget = Widget(self.driver, element_type="NAME", element_locator=self.element_locator)
        assert widget.by == "name", "Element type name not correct"

    def test_get_element_type_link_text(self):
        widget = Widget(self.driver, element_type="LINK_TEXT", element_locator=self.element_locator)
        assert widget.by == "link text", "Element type link text not correct"

    def test_get_element_type_partial_link_text(self):
        widget = Widget(self.driver, element_type="PARTIAL_LINK_TEXT", element_locator=self.element_locator)
        assert widget.by == "partial link text", "Element type partial link text not correct"

    def test_get_element_type_tag_name(self):
        widget = Widget(self.driver, element_type="TAG_NAME", element_locator=self.element_locator)
        assert widget.by == "tag name", "Element type tag name not correct"

    def test_get_element_type_tag_name(self):
        widget = Widget(self.driver, element_type="CLASS_NAME", element_locator=self.element_locator)
        assert widget.by == "class name", "Element type class name not correct"

    def test_get_element_type_css_selector(self):
        widget = Widget(self.driver, element_type="CSS_SELECTOR", element_locator=self.element_locator)
        assert widget.by == "css selector", "Element type css selector not correct"

    @patch.object(Widget, "get_element")
    def test_chrome_get_element(self, patch_get_element):
        widget = Widget(self.driver, element_type="ID", element_locator=self.element_locator)
        widget.get_element()
        assert patch_get_element.called, "Get element method not called"

    @patch.object(Widget, "get_elements")
    def test_chrome_get_elements(self, patch_get_elements):
        widget = Widget(self.driver, element_type="ID", element_locator=self.element_locator)
        widget.get_elements()
        assert patch_get_elements.called, "Get elements method not called"
