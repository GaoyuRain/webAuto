import unittest


def setUpModule():
    print('setUpModule\n')


def tearDownModule():
    print('tearDownModule')


class Test02(unittest.TestCase):
    def setUp(self) -> None:
        print('准备工作')

    def tearDown(self) -> None:
        print('结束工作')

    def test_01(self):
        print('test_01')

    def test_02(self):
        print('test_02')


class Test03(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('start\n')

    @classmethod
    def tearDownClass(cls) -> None:
        print('\nend')

    def setUp(self) -> None:
        print('方法级别：setup')

    def tearDown(self) -> None:
        print('方法级别：teardown')

    def test_01(self):
        print('test_02_01')

    def test_02(self):
        print('test_02_02')
