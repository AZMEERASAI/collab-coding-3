import unittest
from main import function3

class TestFunction3(unittest.TestCase):

    def test_first_two_terms(self):
        """Test that first two Fibonacci numbers are 1"""
        self.assertEqual(function3(1), 1)
        self.assertEqual(function3(2), 1)

    def test_small_fibonacci_numbers(self):
        """Test small Fibonacci numbers"""
        self.assertEqual(function3(3), 2)
        self.assertEqual(function3(4), 3)
        self.assertEqual(function3(5), 5)
        self.assertEqual(function3(6), 8)
        self.assertEqual(function3(7), 13)

    def test_large_fibonacci_number(self):
        """Test a larger Fibonacci number"""
        self.assertEqual(function3(10), 55)
        self.assertEqual(function3(15), 610)

    def test_invalid_input(self):
        """Test invalid (zero or negative) inputs"""
        with self.assertRaises(ValueError):
            function3(0)
        with self.assertRaises(ValueError):
            function3(-5)

if __name__ == "__main__":
    unittest.main()
