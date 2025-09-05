import unittest
from main import function4

class TestFunction4(unittest.TestCase):

    def test_basic_gcd(self):
        """Test GCD of small numbers"""
        self.assertEqual(function4(12, 8), 4)
        self.assertEqual(function4(18, 24), 6)
        self.assertEqual(function4(7, 3), 1)

    def test_with_zero(self):
        """Test cases where one number is zero"""
        self.assertEqual(function4(0, 5), 5)
        self.assertEqual(function4(10, 0), 10)
        self.assertEqual(function4(0, 0), 0)  # conventionally gcd(0,0)=0

    def test_negative_numbers(self):
        """Test GCD with negative numbers (should still be positive)"""
        self.assertEqual(function4(-12, 8), 4)
        self.assertEqual(function4(12, -8), 4)
        self.assertEqual(function4(-12, -8), 4)

    def test_large_numbers(self):
        """Test GCD with large numbers"""
        self.assertEqual(function4(100000, 250000), 50000)
        self.assertEqual(function4(123456, 789012), 12)

if __name__ == "__main__":
    unittest.main()

