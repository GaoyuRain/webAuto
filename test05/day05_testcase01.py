import unittest


def add(a, b):
    return a + b


class TestAdd01(unittest.TestCase):
    def test01_1(self):
        n = add(1, 2)
        print('n01_', n)

    def test01_2(self):
        n = add(2, 2)
        print('n_01', n)
