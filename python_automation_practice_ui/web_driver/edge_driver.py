from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def init_edge_driver():
    return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


class EdgeDriver:
    def __init__(self):
        self.driver = init_edge_driver()
