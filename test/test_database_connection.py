# test_simple_math.py

import unittest

class TestSimpleMath(unittest.TestCase):

    def test_addition(self):
        """Test a simple addition."""
        self.assertEqual(2 + 3, 5)  # 2 + 3 should equal 5

if __name__ == '__main__':
    unittest.main()
