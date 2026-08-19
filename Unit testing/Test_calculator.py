import unittest #unittest 

from calculator import add, substraction, multiply

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2,3),5)

    def test_substraction(self):
        self.assertNotEqual(substraction(4,4),1)

    def test_multiply(self):
        self.assertEqual(multiply(4,4),16)

unittest.main()