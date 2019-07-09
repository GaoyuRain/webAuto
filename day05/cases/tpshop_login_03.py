import sys
import time
import unittest
from time import sleep
import parameterized

from selenium import webdriver


class TestTpShop(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        sleep(3)
        self.driver.quit()

    def test_login(self):
        self.driver.find_element_by_link_text('登录').click()
        self.driver.find_element_by_id('username').send_keys('17645466859')
        self.driver.find_element_by_id('password').send_keys('1234567890')
        self.driver.find_element_by_class_name('J-login-submit').click()
        cont = self.driver.find_element_by_class_name('layui-layer-content').text
        print(cont)
        try:
            self.assertIn('验证码不能!为空', cont)
        except AssertionError as e:
            print('test_login:', e)
            cur_time = time.strftime('%Y%m%d_%H%M%S')
            e_info = sys.exc_info()[1]
            print('test_login:%s_%s' % (cur_time, e_info))
            # self.driver.get_screenshot_as_file('./bugimage/bug_{}_{}.png'.format(cur_time, e_info))
            self.driver.get_screenshot_as_file('../bugimage/bug_test_login_{}_{}.png'.format(*self.bug_info()))
            raise e

    def test_userinfo(self):
        self.driver.find_element_by_link_text('登录').click()
        self.driver.find_element_by_id('username').send_keys('17645466859')
        self.driver.find_element_by_id('password').send_keys('123456')
        self.driver.find_element_by_id('verify_code').send_keys('8888')
        self.driver.find_element_by_class_name('J-login-submit').click()
        user_info = self.driver.find_element_by_class_name('userinfo').text
        try:
            self.assertEqual('117645', user_info)
        except AssertionError as e:
            print('test_userinfo:', e)
            self.driver.get_screenshot_as_file('../bugimage/bug_{}_{}.png'.format(*self.bug_info()))
            raise e

    def bug_info(self):
        cur_time = time.strftime('%Y%m%d_%H%M%S')
        e_info = sys.exc_info()[1]
        print('bug_info:', sys.exc_info())
        return cur_time, str(e_info).replace(':','')
