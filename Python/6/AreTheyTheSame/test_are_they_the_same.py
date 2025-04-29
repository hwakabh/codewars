from unittest import TestCase
from unittest import main

from .are_they_the_same import comp


class TestAreTheyTheSame(TestCase):
    # Test class of are_they_the_same
    def test_comp(self):
        test_patterns = [
            ([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361], True),
            ([4, 4], [1, 31], False),
            ([], None, False),
            ([2, 2, 3], [4, 4, 9], True),
            ([-121, -144, 19, -161, 19, -144, 19, -11], [121, 14641, 20736, 361, 25921, 361, 20736, 361], True),
        ]
        for a1, a2, expected in test_patterns:
            with self.subTest(a1=a1, a2=a2, expected=expected):
                self.assertEqual(comp(array1=a1, array2=a2), expected)


if __name__ == "__main__":
    main(verbosity=2)
