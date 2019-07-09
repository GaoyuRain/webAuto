import unittest


def add(a, b):
    return a + b


class TestAdd02(unittest.TestCase):
    def test02_1(self):
        n = add(1, 2)
        print('n02_', n)
        # e = Exception("test02_2 error:")
        # raise e

    def test02_2(self):
        n = add(2, 2)
        print('n_02', n)
        e = Exception("test02_2 error:")
        raise e
