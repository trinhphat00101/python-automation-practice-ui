from enum import Enum


class PlayGroundUrl(Enum):
    MAIN_PAGE = "http://www.uitestingplayground.com/home"


class PlayGroundId(Enum):
    TITLE = "title"


class PlayGroundXpath(Enum):
    BLOCK_QUOTE = '//*[@id="description"]/descendant::h1[@id="title"]/following::*[@class="blockquote"]/p'
    BLOCK_QUOTE_FOOTER = '//*[@id="description"]/descendant::h1[@id="title"]/following::*[@class="blockquote-footer"]'
    BLOCK_ALERT = '//*[@id="description"]/descendant::h1[@id="title"]/following::div[@class="alert alert-warning"]'
    PAGE_DESCRIPTION = '//*[@id="description"]/descendant::h1[@id="title"]/following::div[@class="alert ' \
                       'alert-warning"]/following::p[1]'
    UI_TAP = '//nav/child::button/preceding::a'
    HOME = '//nav/button/following::div/ul/li[1]/a[contains(@href,"/home")]'
    RESOURCE = '//nav/button/following::div/ul/li[2]/a[contains(@href,"/resources")]'

    DYNAMIC_ID = '//section[@id="overview"]/child::div/child::div[1]/div[1]/descendant::a'
    DYNAMIC_ID_CONTENT = '//section[@id="overview"]/child::div/child::div[1]/div[1]/p'
    CLASS_ATTRIBUTE = '//section[@id="overview"]/child::div/child::div[1]/div[2]/descendant::a'
    CLASS_ATTRIBUTE_CONTENT = '//section[@id="overview"]/child::div/child::div[1]/div[2]/p'
    HIDDEN_LAYER = '//section[@id="overview"]/child::div/child::div[1]/div[3]/descendant::a'
    HIDDEN_LAYER_CONTENT = '//section[@id="overview"]/child::div/child::div[1]/div[3]/p'
    LOAD_DELAY = '//section[@id="overview"]/child::div/child::div[1]/div[4]/descendant::a'
    LOAD_DELAY_CONTENT = '//section[@id="overview"]/child::div/child::div[1]/div[4]/p'

    AJAX_DATA = '//section[@id="overview"]/child::div/child::div[2]/div[1]/descendant::a'
    AJAX_DATA_CONTENT = '//section[@id="overview"]/child::div/child::div[2]/div[1]/p'
    CLIENT_SIDE_DELAY = '//section[@id="overview"]/child::div/child::div[2]/div[2]/descendant::a'
    CLIENT_SIDE_DELAY_CONTENT = '//section[@id="overview"]/child::div/child::div[2]/div[2]/p'
    CLICK = '//section[@id="overview"]/child::div/child::div[2]/div[3]/descendant::a'
    CLICK_CONTENT = '//section[@id="overview"]/child::div/child::div[2]/div[3]/p'
    TEXT_INPUT = '//section[@id="overview"]/child::div/child::div[2]/div[4]/descendant::a'
    TEXT_INPUT_CONTENT = '//section[@id="overview"]/child::div/child::div[2]/div[4]/p'

    SCROLLBARS = '//section[@id="overview"]/child::div/child::div[3]/div[1]/descendant::a'
    SCROLLBARS_CONTENT = '//section[@id="overview"]/child::div/child::div[3]/div[1]/p'
    DYNAMIC_TABLE = '//section[@id="overview"]/child::div/child::div[3]/div[2]/descendant::a'
    DYNAMIC_TABLE_CONTENT = '//section[@id="overview"]/child::div/child::div[3]/div[2]/p'
    VERIFY_TEXT = '//section[@id="overview"]/child::div/child::div[3]/div[3]/descendant::a'
    VERIFY_TEXT_CONTENT = '//section[@id="overview"]/child::div/child::div[3]/div[3]/p'
    PROGRESS_BAR = '//section[@id="overview"]/child::div/child::div[3]/div[4]/descendant::a'
    PROGRESS_BAR_CONTENT = '//section[@id="overview"]/child::div/child::div[3]/div[4]/p'

    VISIBILITY = '//section[@id="overview"]/child::div/child::div[4]/div[1]/descendant::a'
    VISIBILITY_CONTENT = '//section[@id="overview"]/child::div/child::div[4]/div[1]/p'
    SAMPLE_APP = '//section[@id="overview"]/child::div/child::div[4]/div[2]/descendant::a'
    SAMPLE_APP_CONTENT = '//section[@id="overview"]/child::div/child::div[4]/div[2]/p'
    MOUSE_OVER = '//section[@id="overview"]/child::div/child::div[4]/div[3]/descendant::a'
    MOUSE_OVER_CONTENT = '//section[@id="overview"]/child::div/child::div[4]/div[3]/p'
    NON_BREAKING_SPACE = '//section[@id="overview"]/child::div/child::div[4]/div[4]/descendant::a'
    NON_BREAKING_SPACE_CONTENT = '//section[@id="overview"]/child::div/child::div[4]/div[4]/p'

    OVERLAPPED_ELEMENT = '//section[@id="overview"]/child::div/child::div[5]/div[1]/descendant::a'
    OVERLAPPED_ELEMENT_CONTENT = '//section[@id="overview"]/child::div/child::div[5]/div[1]/p'
    SHADOW_DOM = '//section[@id="overview"]/child::div/child::div[5]/div[2]/descendant::a'
    SHADOW_DOM_CONTENT = '//section[@id="overview"]/child::div/child::div[5]/div[2]/p'
    ALERT = '//section[@id="overview"]/child::div/child::div[5]/div[3]/descendant::a'
    ALERT_CONTENT = '//section[@id="overview"]/child::div/child::div[5]/div[3]/p'
    FILE_UPLOAD = '//section[@id="overview"]/child::div/child::div[5]/div[4]/descendant::a'
    FILE_UPLOAD_CONTENT = '//section[@id="overview"]/child::div/child::div[5]/div[4]/p'

    ANIMATED_BUTTON = '//section[@id="overview"]/child::div/child::div[6]/div[1]/descendant::a'
    ANIMATED_BUTTON_CONTENT = '//section[@id="overview"]/child::div/child::div[6]/div[1]/p'
    DISABLED_INPUT = '//section[@id="overview"]/child::div/child::div[6]/div[2]/descendant::a'
    DISABLED_INPUT_CONTENT = '//section[@id="overview"]/child::div/child::div[6]/div[2]/p'
    AUTO_WAIT = '//section[@id="overview"]/child::div/child::div[6]/div[3]/descendant::a'
    AUTO_WAIT_CONTENT = '//section[@id="overview"]/child::div/child::div[6]/div[3]/p'
