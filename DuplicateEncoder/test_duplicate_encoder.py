from unittest import TestCase
from unittest import main

from duplicate_encoder import duplicate_encode


class TestDuplicateEncoder(TestCase):
    # Test class of duplicate_encoder
    def test_duplicate_encode(self):
        test_patterns = [
            ('din', '((('),
            ('recede', '()()()'),
            ('Success', ')())())'),
            ('(( @', '))((')
        ]

        for plain, expected in test_patterns:
            with self.subTest(plain=plain, expected=expected):
                self.assertEqual(duplicate_encode(word=plain), expected)

if __name__ == "__main__":
    main(verbosity=2)