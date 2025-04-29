from unittest import TestCase
from unittest import main

from .very_even_numbers import is_very_even_number


class TestVeryEvenNumbers(TestCase):
    # Test class of very_even_numbers
    def test_is_very_even_number(self):
        test_patterns = [
            (0, True),
            (4,    True ),
            (12,   False),
            (222,  True ),
            (5,    False),
            (45,   False),
            (4554, False),
            (1234, False),
            (88,   False),
            (24,   True ),
            (400000220, True),
        ]
        for number, expected in test_patterns:
            with self.subTest(number=number, expected=expected):
                self.assertEqual(is_very_even_number(n=number), expected)


if __name__ == "__main__":
    main(verbosity=2)
