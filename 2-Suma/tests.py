import unittest
from main import *

# TESTS
class Check(unittest.TestCase):
    # TEST 1 - PRINT A ZERO 
    def test_suma_zero(self):
        test = Suma(0)
        self.assertEqual(test, 0)

    # TEST 2 - PRINT ABOUT SIX 
    def test_suma_six(self):
        test = Suma(6)
        self.assertEqual(test, 8)

    # TEST 3 - PRINT ABOUT TEN 
    def test_suma_ten(self):
        test = Suma(10)
        self.assertEqual(test, 23)

    # TEST 4 - PRINT ABOUT TWENTY 
    def test_suma_twenty(self):
        test = Suma(20)
        self.assertEqual(test, 78)

    # TEST 5 - PRINT ABOUT 100 
    def test_suma_hundred(self):
        test = Suma(100)
        self.assertEqual(test, 2318)


if __name__ == "__main__":
    unittest.main()