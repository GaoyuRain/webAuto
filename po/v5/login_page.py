from selenium.webdriver.common.by import By

from utils import DriverUtils

'''登录模块'''


class LoginPage(object):
    '''对象库层'''

    def __init__(self):
        self.driver = DriverUtils.get_driver()
        self.username = (By.ID, 'username')
        self.password = (By.ID, 'password')
        self.verify_code = (By.ID, 'verify_code')
        self.login_btn = (By.CLASS_NAME, 'J-login-submit')
        self.main_login_btn = (By.LINK_TEXT, '登录')

    def find_username(self):
        return self.driver.find_element(*self.username)

    def find_password(self):
        return self.driver.find_element(*self.password)

    def find_verify_code(self):
        return self.driver.find_element(*self.verify_code)

    def find_login_login_btn(self):
        return self.driver.find_element(*self.login_btn)

    def find_main_login_btn(self):
        '''首页登录按钮'''
        return self.driver.find_element(*self.main_login_btn)


class LoginHandle(object):
    '''对象操作层'''

    def __init__(self):
        self.login_page = LoginPage()

    def click_main_login_btn(self):
        self.login_page.find_main_login_btn().click()

    def input_username(self, username):
        self.login_page.find_username().clear()
        self.login_page.find_username().send_keys(username)

    def input_password(self, password):
        self.login_page.find_password().clear()
        self.login_page.find_password().send_keys(password)

    def input_verify_code(self, code):
        self.login_page.find_verify_code().clear()
        self.login_page.find_verify_code().send_keys(code)

    def click_login_login_btn(self):
        self.login_page.find_login_login_btn().click()


class LoginProxy(object):
    """对象业务层"""

    def __init__(self):
        self.driver = DriverUtils.get_driver()
        self.login_handle = LoginHandle()

    def init_login(self):
        '''跳转到登录页面'''
        DriverUtils.get_driver().get('http://localhost/')
        self.login_handle.click_main_login_btn()

    def login(self, username, password, code):
        self.login_handle.input_username(username)
        self.login_handle.input_password(password)
        self.login_handle.input_verify_code(code)
        self.login_handle.click_login_login_btn()


if __name__ == '__main__':
    class Test1(object):
        count = 0


    test1 = Test1()
    test2 = Test1()
    print(id(test1.count))
    test1.count = 2
    print(test2.count)
    print(id(test1.count))
    print(id(test2.count))

    Test1.count = 3
    print(test2.count)
    print(test1.count)
    print(id(test1.count))
    print(id(test2.count))


    def text01(a, *args):
        result = a + args[0] + args[1]
        print(result)


    data = (2, 4)
    text01(1, data)
