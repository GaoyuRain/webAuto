import unittest
from time import sleep

from selenium import webdriver

from utils import DriverUtils, get_tips_msg


class TestTpShopLogin(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtils.get_driver()

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(3)
        DriverUtils.quit_driver()

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
        cont = get_tips_msg()
        print(cont)
        self.assertIn('账号不存在', cont)

    def test_wrong_password(self):
        self.driver.find_element_by_id('username').send_keys('17645466859')
        self.driver.find_element_by_id('password').send_keys('1234567890')
        self.driver.find_element_by_id('verify_code').send_keys('8888')
        self.driver.find_element_by_class_name('J-login-submit').click()
        cont = get_tips_msg()
        print(cont)
        self.assertIn('密码错误', cont)
