from unittest import TestCase
from unittest import main

from what_is_your_poison import find


class TestWhatIsYourPoison(TestCase):
    # Test class of what_is_your_poison
    def test_find(self):
        test_patterns = [
            ([0, 3, 5, 4, 9, 8], 825),
            ([0, 1, 9, 3, 5], 555),
            ([0, 1, 2, 3, 4, 6], 95),
            ([0, 1, 3, 4], 27),
        ]

        for r, expected in test_patterns:
            with self.subTest(r=r, expected=expected):
                self.assertEqual(find(r=r), expected)


if __name__ == "__main__":
    main(verbosity=2)
