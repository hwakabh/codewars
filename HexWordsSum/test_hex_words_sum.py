from unittest import TestCase
from unittest import main

from hex_words_sum import hex_word_sum


class TestHexWordsSum(TestCase):
    # Test class of hex_words_sum
    def test_hex_word_sum(self):
        test_patterns = [
            ('DEFACE', 14613198),
            ('SAFE', 23294),
            ('CODE', 49374),
            ('BUGS', 0),
            ('', 0),
            ('DO YOU SEE THAT BEE DRINKING DECAF COFFEE', 13565769),
            ('ASSESS ANY BAD CODE AND TRY AGAIN', 10889952),
            # ('BUGS OF BEES', 0)  #-> Wrong Case: should work with multiple words if contains invalid hex
        ]

        for strings, expected in test_patterns:
            with self.subTest(strings=strings, expected=expected):
                self.assertEqual(hex_word_sum(string=strings), expected)


if __name__ == "__main__":
    main(verbosity=2)