import unittest

def div(a,b):
    return a/b

class testdiv(unittest.TestCase):
    def check_div(self):
        with self.assertRaises(ZeroDivisionError):
            div(10,0)

unittest.main()


import unittest


def divide(a, b):
    return a / b


class TestDivide(unittest.TestCase):

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


unittest.main()