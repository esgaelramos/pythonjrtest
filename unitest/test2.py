import unittest
from test import hola

# UNITTEST

# TESTCASE:
# COLECCION DE UNITEST

# assert method: checha que el resultado que recibiste coíncide con el que esperabas

class checar(unittest.TestCase):
    def test_holis(self):
        b = hola('lola', 18)
        self.assertEqual(b, "Hola mi nombre es lola y tengo 18 años.")

if __name__ == "__main__":
    unittest.main()