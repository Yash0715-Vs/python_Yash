import unittest


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.marks = [55, 66, 77]

    def tearDown(self):
        self.marks = []

    def test_length(self):
        self.assertEqual(len(self.marks), 3)

    def test_first_marks(self):
        self.assertEqual(self.marks[2], 77)


unittest.main()
    
    

