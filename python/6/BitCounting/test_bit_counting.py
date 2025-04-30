from unittest import TestCase
from unittest import main

from .bit_counting import countBits

class TestBitCounting(TestCase):
    # Test Class of bit_counting
    def test_countBits(self):
        test_patterns = [
            (1234, 5),
            (0, 0),
            (4, 1),
            (7, 3),
            (9, 2),
            (10, 2),
            # (12345, 5) #-> Wrong Case: Binary of 12345 == 11000000111001, since bits == 6
        ]

        for num, bits in test_patterns:
            with self.subTest(num=num, bits=bits):
                self.assertEqual(countBits(n=num), bits)


if __name__ == '__main__':
    main(verbosity=2)
