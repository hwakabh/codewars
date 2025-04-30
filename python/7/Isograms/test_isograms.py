import unittest

from .isograms import is_isogram

class TestIsogram(unittest.TestCase):
    # Test class of isograms.py

    def test_is_isogram(self):
        test_patterns = [
            ('Dermatoglyphics', True),   #-> Expected True
            ('isogram', True),   #-> Expected True
            ('aba', False),   #-> Expected False (duplicated with 'a')
            ('moOse', False),   #-> Expected False (duplicated with 'o'/'O')
            # ('Aa', True),  #-> Wrong Case
            ('isIsogram', False),  #-> Expected False (duplicated with 'i'/'I')
            ('', True),  #-> Expected True (empty string is valid isogram)
        ]

        for input_value, expected in test_patterns:
            # print('Testing with paramter {0} : expected {1}'.format(input_value, expected))
            with self.subTest(input_value=input_value, expected=expected):
                self.assertEqual(is_isogram(string=input_value), expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
