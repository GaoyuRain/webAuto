from time import sleep

from selenium import webdriver


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
        print('quit_driver:', cls.__driver)
        if cls.__driver:
            print('quit_driver')
            sleep(3)
            cls.__driver.quit()
            cls.__driver = None
