"""
author :Rain
Date : 2019/07/04
Description : 前台登录模块测试case
"""
import time
import unittest

from test.login_page import LoginProxy
from test.utils import DriverUtils, get_user_name


class TestTpShopLoginPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtils.get_driver()
        cls.login_proxy = LoginProxy()

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtils.quit_driver()

    def setUp(self) -> None:
        self.driver.get('http://localhost/')
        self.driver.find_element_by_link_text('登录').click()

    def tearDown(self) -> None:
        pass

    def test_login_sucess(self):
        self.login_proxy.login('17645466859', '123456', '8888')
        user_name = get_user_name()
        try:
            self.assertIn('17645466859', user_name)
        except AssertionError as error:
            print(error)
            self.driver.get_screenshot_as_file('./test_login_sucess_fail_{}.png'.format(time.strftime('%Y%m%d_%H%M%S')))
            raise error


if __name__ == '__main__':
    unittest.main()
