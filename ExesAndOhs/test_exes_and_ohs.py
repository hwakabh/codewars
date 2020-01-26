from unittest import TestCase
from unittest import main

from exes_and_ohs import xo


class TestExesAndOhs(TestCase):
    # Test class of exes_and_ohs
    def test_xo(self):
        test_patterns = [
            ('ooxx', True),
            ('xooxx', False),
            ('ooxXm', True),
            ('zpzpzpp', True),
            ('zzoo', False),
            # ('xxXxooO0', True) #-> Wrong Case: x=4, o=3
        ]

        for string, expected in test_patterns:
            with self.subTest(string=string, expected=expected):
                self.assertEqual(xo(s=string), expected)


if __name__ == "__main__":
    main(verbosity=2)