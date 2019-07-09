import time
import unittest

from HTMLTestRunnerCN import HTMLTestReportCN
from day08.calc2.test_calc import TestCalc


def get_report():
    # mysuite = unittest.TestSuite()
    # mysuite.addTest(TestCalc('test_add'))
    mysuite = unittest.defaultTestLoader.discover('./', pattern='test_calc.py')
    with open('./calc_test_report_{}.html'.format(time.strftime("%Y%m%d_%H%M%S")), 'wb') as f:
        HTMLTestReportCN(f, verbosity=2, title='计算机加法测试报告').run(mysuite)


if __name__ == '__main__':
    get_report()
