import unittest
from main import function5

class TestFunction5(unittest.TestCase):

    def test_basic_strings(self):
        """Test simple string reversals"""
        self.assertEqual(function5("hello"), "olleh")
        self.assertEqual(function5("abc"), "cba")

    def test_palindrome(self):
        """Test that palindromes remain the same when reversed"""
        self.assertEqual(function5("madam"), "madam")
        self.assertEqual(function5("racecar"), "racecar")

    def test_empty_and_single_char(self):
        """Test empty string and single character"""
        self.assertEqual(function5(""), "")
        self.assertEqual(function5("a"), "a")

    def test_with_spaces_and_numbers(self):
        """Test strings with spaces and numbers"""
        self.assertEqual(function5("12345"), "54321")
        self.assertEqual(function5("hello world"), "dlrow olleh")

if __name__ == "__main__":
    unittest.main()
