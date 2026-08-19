# import unittest

# def div(a,b):
#     return a/b

# class testdiv(unittest.TestCase):
#     def check_div(self):
#         with self.assertRaises(ZeroDivisionError):
#             div(10,0)

# unittest.main() # it shows no test runs because unittest always starts with test method(test_check) not (check_div).


import unittest


def divide(a, b):
    return a / b


class TestDivide(unittest.TestCase):

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


unittest.main()