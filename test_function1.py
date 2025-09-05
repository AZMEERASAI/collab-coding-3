import unittest
from main import function1

class TestFunction1(unittest.TestCase):

    def test_factorial_basic(self):
        self.assertEqual(function1(0), 1)
        self.assertEqual(function1(1), 1)
        self.assertEqual(function1(5), 120)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            function1(-5)

    def test_factorial_non_integer(self):
        with self.assertRaises(TypeError):
            function1(3)

if __name__ == "__main__":
    unittest.main()

