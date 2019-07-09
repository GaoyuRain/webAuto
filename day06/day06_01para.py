import unittest
from parameterized import parameterized


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def add_data():
    return [(1, 2, 3), (2, 3, 5), (0, 0, 0), (5, 5, 10)]


class Test01(unittest.TestCase):
    sub_data = [(2, 1, 1), (1, 1, 1), (2, 2, 0)]

    @parameterized.expand([(1, 2, 3), (2, 3, 4), (0, 0, 1)])
    def test_add(self, x, y, expect):
        result = add(x, y)
        print(result)
        try:
            self.assertEqual(result, expect)
        except AssertionError as e:
            print('test_add error_', e)
            raise e

    @parameterized.expand(add_data())
    def test_add01(self, x, y, expect):
        result = add(x, y)
        self.assertEqual(result, expect)

    @parameterized.expand(sub_data)
    def test_sub(self, x, y, expect):
        result = sub(x, y)
        self.assertEqual(expect, result)
