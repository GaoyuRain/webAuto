import unittest
import json
from time import sleep

from day07.calc.calc_page import CalcProxy
from day07.calc.utils import DriverUtils, get_result
from parameterized import parameterized
from HTMLTestRunnerCN import HTMLTestReportCN


def get_data(type):
    '''
    获取加减乘除数据
    :param type: 1 加 ，2 减 ，3 乘 ， 4 除
    :return:
    '''
    with open('./calc_test_data.json', encoding='utf-8') as f:
        dict_data = json.load(f)
        # print(dict_data)
    if type == 1:
        return tuple(dict_data.get('add'))
    elif type == 2:
        return tuple(dict_data.get('sub'))
    elif type == 3:
        return tuple(dict_data.get('muliti'))
    elif type == 4:
        return tuple(dict_data.get('divi'))


class TestCalc(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.calc_proxy = CalcProxy()

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtils.quit_driver()
        HTMLTestReportCN()

    @parameterized.expand(get_data(1))
    def test_add(self, x, y, z):
        self.calc_proxy.add(x, y)
        sleep(2)
        result = get_result()
        print('result', result)
        self.assertEqual(str(z), result)

    # @unittest.skip('未实现 减法 用例编写')
    @parameterized.expand(get_data(2))
    def test_sub(self, x, y, z):
        self.calc_proxy.sub(x, y)
        sleep(2)
        result = get_result()
        print('result', result)
        self.assertEqual(str(z), result)

    # @unittest.skip('未实现 乘法 用例编写')
    @parameterized.expand(get_data(3))
    def test_multi(self, x, y, z):
        self.calc_proxy.multi(x, y)
        sleep(2)
        result = get_result()
        print(x, y, z)
        print('result', result)
        self.assertEqual(str(z), result)

    # @parameterized.expand(get_data(4))
    @unittest.skip('未实现 除法 用例编写')
    def test_divi(self, x, y, z):
        pass


if __name__ == '__main__':
    print(get_data(1))
