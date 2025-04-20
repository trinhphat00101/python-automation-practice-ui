import logging

from python_automation_practice_ui.page_object.web_locator.playground_locator import PlayGroundUrl, PlayGroundId, \
    PlayGroundXpath
from selenium.webdriver.common.by import By


class PlaygroundMainPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger()

    def open(self):
        self.logger.info("Open main page")
        self.driver.get(PlayGroundUrl.MAIN_PAGE.value)

    def title_element(self):
        self.logger.info("Get title element")
        return self.driver.find_element(By.ID, PlayGroundId.TITLE.value)

    def title_text(self):
        self.logger.info("Get title text")
        var = self.title_element().text
        return var

    def block_quote_element(self):
        self.logger.info("Get block quote element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.BLOCK_QUOTE.value)

    def block_quote_text(self):
        self.logger.info("Get block quote text")
        return self.block_quote_element().text

    def block_quote_footer_element(self):
        self.logger.info("Get quote footer element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.BLOCK_QUOTE_FOOTER.value)

    def block_quote_footer_text(self):
        self.logger.info("Get quote footer text")
        return self.block_quote_footer_element().text

    def block_quote_alert_element(self):
        self.logger.info("Get quote alert element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.BLOCK_ALERT.value)

    def block_quote_alert_text(self):
        self.logger.info("Get quote alert text")
        return self.block_quote_alert_element().text

    def description_element(self):
        self.logger.info("Get description element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.PAGE_DESCRIPTION.value)

    def description_text(self):
        self.logger.info("Get description text")
        return self.description_element().text

    def ui_tap_element(self):
        self.logger.info("Get Ui Tap element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.UI_TAP.value)

    def home_element(self):
        self.logger.info("Get Home element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.HOME.value)

    def resources_element(self):
        self.logger.info("Get Resources element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.RESOURCE.value)

    def dynamic_id_element(self):
        self.logger.info("Get Dynamic id element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.DYNAMIC_ID.value)

    def dynamic_id_content_element(self):
        self.logger.info("Get Dynamic id content")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.DYNAMIC_ID_CONTENT.value)

    def class_element(self):
        self.logger.info("Get Class element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.CLASS_ATTRIBUTE.value)

    def class_attribute_element(self):
        self.logger.info("Get Class Attribute")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.CLASS_ATTRIBUTE_CONTENT.value)

    def hidden_layer_element(self):
        self.logger.info("Get Hidden layer attribute")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.HIDDEN_LAYER.value)

    def hidden_layer_content_element(self):
        self.logger.info("Get Hidden layer content element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.HIDDEN_LAYER_CONTENT.value)

    def load_delay_element(self):
        self.logger.info("Get load delay element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.LOAD_DELAY.value)

    def load_delay_content_element(self):
        self.logger.info("Get Load delay content element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.LOAD_DELAY_CONTENT.value)

    def ajax_data_element(self):
        self.logger.info("Get Ajax data element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.AJAX_DATA.value)

    def ajax_data_content_element(self):
        self.logger.info("Get Ajax data content element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.AJAX_DATA_CONTENT.value)

    def client_side_delay_element(self):
        self.logger.info("Get Client side delay element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.CLIENT_SIDE_DELAY.value)

    def client_side_delay_content_element(self):
        self.logger.info("Get Client Side delay content element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.CLIENT_SIDE_DELAY_CONTENT.value)

    def click_element(self):
        self.logger.info("Get click element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.CLICK.value)

    def click_content_element(self):
        self.logger.info("Get click content element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.CLICK_CONTENT.value)

    def text_input_element(self):
        self.logger.info("Get text input element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.TEXT_INPUT.value)

    def text_input_content_element(self):
        self.logger.info("Get text input content element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.TEXT_INPUT_CONTENT.value)

    def scrollbars_element(self):
        self.logger.info("Get scrollbars element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.SCROLLBARS.value)

    def scrollbars_content_element(self):
        self.logger.info("Get scrollbars content element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.SCROLLBARS_CONTENT.value)

    def dynamic_table_element(self):
        self.logger.info("Get dynamic table element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.DYNAMIC_TABLE.value)

    def dynamic_table_content_element(self):
        self.logger.info("Get dynamic table content element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.DYNAMIC_TABLE_CONTENT.value)

    def verify_text_element(self):
        self.logger.info("Get verify text element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.VERIFY_TEXT.value)

    def verify_text_content_element(self):
        self.logger.info("Get verify text content element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.VERIFY_TEXT_CONTENT.value)

    def progress_bar_element(self):
        self.logger.info("Get progress bar element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.PROGRESS_BAR.value)

    def progress_bar_content_element(self):
        self.logger.info("Get progress bar content element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.PROGRESS_BAR_CONTENT.value)

    def visibility_element(self):
        self.logger.info("Get visibility element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.VISIBILITY.value)

    def visibility_content_element(self):
        self.logger.info("Get visibility content element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.VISIBILITY_CONTENT.value)

    def sample_app_element(self):
        self.logger.info("Get sample app element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.SAMPLE_APP.value)

    def sample_app_content_element(self):
        self.logger.info("Get sample app content element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.SAMPLE_APP_CONTENT.value)

    def mouse_over_element(self):
        self.logger.info("Get mouse over element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.MOUSE_OVER.value)

    def mouse_over_content_element(self):
        self.logger.info("Get mouse over content element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.MOUSE_OVER_CONTENT.value)

    def non_breaking_space_element(self):
        self.logger.info("Get non breaking space element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.NON_BREAKING_SPACE.value)

    def non_breaking_space_content_element(self):
        self.logger.info("Get non breaking space content element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.NON_BREAKING_SPACE_CONTENT.value)

    def overlapped_element_element(self):
        self.logger.info("Get overlapped element element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.OVERLAPPED_ELEMENT.value)

    def overlapped_element_content_element(self):
        self.logger.info("Get overlapped element content element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.OVERLAPPED_ELEMENT_CONTENT.value)

    def shadow_dom_element(self):
        self.logger.info("Get shadow dom element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.SHADOW_DOM.value)

    def shadow_dom_content_element(self):
        self.logger.info("Get shadow dom content element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.SHADOW_DOM_CONTENT.value)

    def alert_element(self):
        self.logger.info("Get alert element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.ALERT.value)

    def alert_content_element(self):
        self.logger.info("Get alert content element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.ALERT_CONTENT.value)

    def file_upload_element(self):
        self.logger.info("Get file upload element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.FILE_UPLOAD.value)

    def file_upload_content_element(self):
        self.logger.info("Get file upload content element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.FILE_UPLOAD_CONTENT.value)

    def animated_button_element(self):
        self.logger.info("Get animated button element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.ANIMATED_BUTTON.value)

    def animated_button_content_element(self):
        self.logger.info("Get animated button content element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.ANIMATED_BUTTON_CONTENT.value)

    def disabled_input_element(self):
        self.logger.info("Get disabled input element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.DISABLED_INPUT.value)

    def disabled_input_content_element(self):
        self.logger.info("Get disabled input content element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.DISABLED_INPUT_CONTENT.value)

    def auto_wait_element(self):
        self.logger.info("Get auto wait element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.AUTO_WAIT.value)

    def auto_wait_content_element(self):
        self.logger.info("Get auto wait content element")
        return self.driver.find_element(By.XPATH, PlayGroundXpath.AUTO_WAIT_CONTENT.value)
