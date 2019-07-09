from selenium.webdriver.remote.webelement import WebElement

from day08.calc2.utils import DriverUtils


class CalcBasePage:
    '''对象库层基类'''

    def __init__(self):
        self.driver = DriverUtils.get_driver()

    def find_element(self, location):
        return self.driver.find_element(*location)


class CalcBaseHandle:
    def click_element(self, element: WebElement):
        element.click()
