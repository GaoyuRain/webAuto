import time

from parameterized import parameterized
import unittest

from HTMLTestRunnerCN import HTMLTestReportCN


def add(x, y):
    return x + y


def get_add_data():
    data = [(1, 1, 2), (2, 3, 6), (2, 2, 4)]
    return data


version = 30

# class TestDay06(unittest.TestCase):
#
#     @parameterized.expand(get_add_data())
#     def test_add(self, x, y, z):
#         result = add(x, y)
#         self.assertEqual(result, z)
#
#     def test01(self):
#         print('test01')
#
#     @unittest.skip('跳过test02')
#     def test02(self):
#         print('test02')
#
#     def test03(self):
#         print('test03')
#
#     @unittest.skipIf(version > 20, '版本号过大跳过04')
#     def test04(self):
#         print('test04')


if __name__ == '__main__':
    mysuite = unittest.defaultTestLoader.discover('../testcases/', pattern='*.py')

    with open('../testreport/tpshop_test_report_{}.html'.format(time.strftime('%Y%m%d_%H%M%S')), 'wb') as f:
        runner = HTMLTestReportCN(stream=f, verbosity=2, title='tpshop登录模块测试报告', description='windows环境,等等等',
                                  tester='Rain')
        runner.run(mysuite)
