"""
author :Rain
Date : 2019/07/04
Description :前台登录页面po
"""
from selenium.webdriver.common.by import By

from test.base_page import BasePage, BaseHandle


class LoginPage(BasePage):
    '''对象库层'''

    def __init__(self):
        super().__init__()
        self.username = (By.ID, 'username')
        self.password = (By.ID, 'password')
        self.verify_code = (By.ID, 'verify_code')
        self.login_btn = (By.CLASS_NAME, 'J-login-submit')

    def find_username(self):
        return self.find_element(self.username)

    def find_password(self):
        return self.find_element(self.password)

    def find_verify_code(self):
        return self.find_element(self.verify_code)

    def find_login_login_btn(self):
        return self.find_element(self.login_btn)


class LoginHandle(BaseHandle):
    '''对象操作层'''

    def __init__(self):
        self.login_page = LoginPage()

    def input_username(self, username):
        self.input_test(self.login_page.find_username(), username)

    def input_password(self, password):
        self.input_test(self.login_page.find_password(), password)

    def input_verify_code(self, code):
        self.input_test(self.login_page.find_verify_code(), code)

    def click_login_login_btn(self):
        self.login_page.find_login_login_btn().click()


class LoginProxy(object):
    """对象业务层"""

    def __init__(self):
        self.login_handle = LoginHandle()

    def login(self, username, password, code):
        self.login_handle.input_username(username)
        self.login_handle.input_password(password)
        self.login_handle.input_verify_code(code)
        self.login_handle.click_login_login_btn()
