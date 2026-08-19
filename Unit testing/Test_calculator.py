import unittest #unittest 

from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def tearDown(self):
        print("test completed")

    def test_add(self):
        self.assertEqual(self.calculator.add(2,3),5)

    def test_substraction(self):
        self.assertNotEqual(self.calculator.substraction(4,4),1)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(4,4),16)

    def test_square(self):
        self.assertEqual(self.calculator.square(5), 25)
unittest.main()