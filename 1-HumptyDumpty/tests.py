import unittest
from main import *

# TESTS
class Check(unittest.TestCase):
    # TEST 1 - PRINT A EMPTY LIST 
    def test_humpty_zero(self):
        test = Humpty(0)
        self.assertEqual(test, [])

    # TEST 1 - PRINT A 5 LIST 
    def test_humpty_five(self):
        test = Humpty(5)
        self.assertEqual(test, ['1', '2', 'Humpty', '4', 'Dumpty'])

    # TEST 3 - PRINT A 10 LIST
    def test_humpty_ten(self):
        test = Humpty(10)
        self.assertEqual(test, ['1', '2', 'Humpty', '4', 'Dumpty', 'Humpty', '7', '8', 'Humpty', 'Dumpty'])

    # TEST 4 - PRINT A 15 LIST
    def test_humpty_fifteen(self):
        test = Humpty(15)
        self.assertEqual(test, ['1', '2', 'Humpty', '4', 'Dumpty', 'Humpty', '7', '8', 'Humpty', 'Dumpty', '11', 'Humpty', '13', '14', 'HumptyDumpty'])

    # TEST 5 - PRINT A 30 LIST
    def test_humpty_thirty(self):
        test = Humpty(30)
        self.assertEqual(test, ['1', '2', 'Humpty', '4', 'Dumpty', 'Humpty', '7', '8', 'Humpty', 'Dumpty', '11', 'Humpty', '13', '14', 'HumptyDumpty', '16', '17', 'Humpty', '19', 'Dumpty', 'Humpty', '22', '23', 'Humpty', 'Dumpty', '26', 'Humpty', '28', '29', 'HumptyDumpty'])


if __name__ == "__main__":
    unittest.main()