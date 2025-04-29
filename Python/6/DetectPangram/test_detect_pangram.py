from unittest import TestCase
from unittest import main

from .detect_pangram import is_pangram


class TestDetectPangram(TestCase):
    def test_is_pangram(self):
        test_patterns = [
            ('The quick, brown fox jumps over the lazy dog!', True),
            ('Cwm fjord bank glyphs vext quiz', True),
            ('abcdefghijklmopqrstuvwxyz', False),
        ]
        for inp, exp in test_patterns:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(is_pangram(s=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
