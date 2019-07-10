from selenium.webdriver.remote.webelement import WebElement

from test08.tp_shop_login.utils import DriverUtils


class BasePage:
    def __init__(self):
        self.driver = DriverUtils.get_driver()

    def find_element(self, location):
        return self.driver.find_element(*location)


class BaseHandle:

    @staticmethod
    def input_test(element: WebElement, cont):
        element.clear()
        element.send_keys(cont)
