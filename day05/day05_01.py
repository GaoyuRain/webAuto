import unittest

from day05.day05_testcase01 import TestAdd01
from day05.day05_testcase02 import TestAdd02


def text01():
    mysuite = unittest.TestSuite()
    mysuite.addTest(TestAdd01('test01_1'))
    mysuite.addTest(TestAdd01('test01_2'))
    mysuite.addTest(unittest.makeSuite(TestAdd02))
    runner = unittest.TextTestRunner()
    runner.run(mysuite)


def text02():
    mysuite = unittest.defaultTestLoader.discover('./cases/', 'soft*.py')
    unittest.TextTestRunner().run(mysuite)


def text03():
    mysuite = unittest.defaultTestLoader.discover('./cases/', 'tpshop*.py')
    unittest.TextTestRunner().run(mysuite)


if __name__ == '__main__':
    text03()
