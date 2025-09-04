import unittest
from main import function1

class TestFunction1(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(function1(5), 120)
        self.assertEqual(function1(0), 1)
        with self.assertRaises(ValueError):
            function1(-1)

if _name_ == "_main_":
    unittest.main()