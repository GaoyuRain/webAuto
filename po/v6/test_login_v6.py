import unittest
from time import sleep

from po.v6.login_page import LoginProxy
from utils import DriverUtils, get_tips_msg


class TestTpShopLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_proxy = LoginProxy()

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(3)
        DriverUtils.quit_driver()

    def setUp(self) -> None:
        '''进入登录页面'''
        self.login_proxy.init_login()

    def tearDown(self) -> None:
        sleep(3)

    def test_account_not_esist(self):
        self.login_proxy.login('16645466859', '1234567890', '8888')
        cont = get_tips_msg()
        print(cont)
        sleep(1)
        self.assertIn('账号不存在', cont)

    def test_wrong_password(self):
        self.login_proxy.login('17645466859', '1234567890', '8888')
        cont = get_tips_msg()
        print(cont)
        self.assertIn('密码错误', cont)
