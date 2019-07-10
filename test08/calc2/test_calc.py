import json
import time
import unittest

from test08.calc2.calc_page import CalcProxy
from test08.calc2.utils import DriverUtils
from parameterized import parameterized
from HTMLTestRunnerCN import HTMLTestReportCN


def get_data():
    with open('./calc_test_data.json', encoding='utf-8') as f:
        data = json.load(f)
    return data


class TestCalc(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.calc_proxy = CalcProxy()

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')
        DriverUtils.quit_driver()


    @parameterized.expand(get_data())
    def test_add(self, x, y, expt):
        self.calc_proxy.add(x, y)
        result = self.calc_proxy.get_result_func()
        self.assertEqual(str(expt), result)


if __name__ == '__main__':
    unittest.main()
