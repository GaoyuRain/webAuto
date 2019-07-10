from time import sleep

from selenium import webdriver


def get_result():
    return DriverUtils.get_driver().find_element_by_id('resultIpt').get_attribute("value")


class DriverUtils:
    __driver = None

    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.get('http://cal.apple886.com/')
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(15)
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        if cls.__driver:
            sleep(3)
            cls.__driver.quit()
            cls.__driver = None
