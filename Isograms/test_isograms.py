import unittest
from isograms import is_isogram

class TestIsogram(unittest.TestCase):
    # Test class of isograms.py
    def test_is_isogram(self):
        test_value = 'Dermatoglyphics'
        expected = True
        actual = is_isogram(string=test_value)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
