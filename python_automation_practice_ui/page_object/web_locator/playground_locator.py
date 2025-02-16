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
