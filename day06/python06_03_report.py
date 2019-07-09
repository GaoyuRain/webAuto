# from HTMLTestRunner import HTMLTestRunner
import unittest
import time
from HTMLTestRunner import HTMLTestRunner


# def get_day06_report01():
#     suite = unittest.defaultTestLoader.discover('../testcases')
#     report_path = '../testreport/test_report_{}.HTML'.format(time.strftime('%Y%m%d_%H%M%S'))
#     HTMLTestRunner(output='report_path').run(suite)
#     with open(report_path, 'wb') as f:
#         HTMLTestRunner(output='report_path').run(suite)


def get_day06_report02():
    suite = unittest.defaultTestLoader.discover('../testcases', pattern='*.py')
    report_path = '../testreport/test_report_{}.html'.format(time.strftime('%Y%m%d_%H%M%S'))
    with open(report_path, 'wb') as f:
        HTMLTestRunner(stream=f, title='day05自动化测试报告', description='chrome浏览器，window系统，测试所有用例', verbosity=2).run(suite)


if __name__ == '__main__':
    get_day06_report02()
