from unittest import TestCase
from unittest import main

from making_change import make_change


class TestMakingChange(TestCase):
    # Test class of making_change
    def test_make_change(self):
        test_patterns = [
            (0, {}),
            (1, {'P': 1}),
            (43, {'Q': 1, 'D': 1, 'N': 1, 'P': 3}),
            (91, {'H': 1, 'Q': 1, 'D': 1, 'N': 1, 'P': 1}),
        ]
        for a, expected in test_patterns:
            with self.subTest(a=a, expected=expected):
                self.assertEqual(make_change(amount=a), expected)


if __name__ == '__main__':
    main(verbosity=2)
