import unittest
from time import sleep

from selenium import webdriver


class TestTpShopLogin(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://localhost/')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(3)
        cls.driver.quit()

    def setUp(self) -> None:
        self.driver.get('http://localhost/')
        self.driver.find_element_by_link_text('登录').click()

    def tearDown(self) -> None:
        sleep(3)

    def test_account_not_esist(self):
        self.driver.find_element_by_id('username').send_keys('16645466859')
        self.driver.find_element_by_id('password').send_keys('1234567890')
        self.driver.find_element_by_id('verify_code').send_keys('8888')
        self.driver.find_element_by_class_name('J-login-submit').click()
        cont = self.driver.find_element_by_class_name('layui-layer-content').text
        print(cont)
        self.assertIn('账号不存在', cont)

    def test_wrong_password(self):
        self.driver.find_element_by_id('username').send_keys('17645466859')
        self.driver.find_element_by_id('password').send_keys('1234567890')
        self.driver.find_element_by_id('verify_code').send_keys('8888')
        self.driver.find_element_by_class_name('J-login-submit').click()
        cont = self.driver.find_element_by_class_name('layui-layer-content').text
        print(cont)
        self.assertIn('密码错误', cont)
