from unittest import TestCase
from unittest import main

from .array_exchange import exchange_with


class TestArrayExchange(TestCase):
    # Test class of array_exchange
    def test_exchange_with(self):
        test_patterns = [
            (['1', '2', '3', '4', '5', '6', '7'], ['a', 'b', 'c'], (['c', 'b', 'a'], ['7', '6', '5', '4', '3', '2', '1'])),
        ]
        for a, b, expected in test_patterns:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(exchange_with(a=a, b=b), expected)


if __name__ == "__main__":
    main(verbosity=2)
