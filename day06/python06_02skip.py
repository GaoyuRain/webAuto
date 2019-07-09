import unittest
from parameterized import parameterized

version = 30


def add(a, b):
    return a + b


def add_data():
    return [(1, 2, 3), (2, 3, 5), (0, 0, 0), (5, 5, 10)]


class Test01(unittest.TestCase):

    def test01(self):
        print('test01')

    @unittest.skip('跳过test02')
    def test02(self):
        print('test02')

    @unittest.skipIf(version > 25, '版本过高跳过')
    def test03(self):
        print('test03')

    @unittest.skipUnless(False, 'skipUnless跳过')
    def test04(self):
        print('test04')

    @parameterized.expand(add_data())
    def test_add01(self, x, y, expect):
        result = add(x, y)
        self.assertEqual(result, expect)


@unittest.skip('代码未完成')
class Test02(unittest.TestCase):

    def test01(self):
        print('Test02_test01')

    def test02(self):
        print('Test02_test02')

    def test03(self):
        print('Test02_test03')
