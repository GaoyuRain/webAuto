import json
import unittest
from time import sleep
from parameterized import parameterized

from day08.tp_shop_login.login_page import LoginProxy
from day08.tp_shop_login.utils import DriverUtils, get_tips_msg


def get_data():
    with open('./test_tp_shop_data.json', encoding='utf-8') as f:
        data = json.load(f)
        return [x.values() for x in data.values()]


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

    # ['', '123456', '8888', False, '用户名不能为空']
    @parameterized.expand(get_data())
    def test_login(self, name, pwd, code, is_sucess, expc):
        self.login_proxy.login(name, pwd, code)
        sleep(2)
        result = get_tips_msg(is_sucess)
        print('result:', result, ',expect:', expc)
        self.assertIn(expc, result)
