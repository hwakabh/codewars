from unittest import TestCase
from unittest import main

from .number_of_occurrence import number_of_occurrence


class TestNumberOfOccurrence(TestCase):
    # Test class of number_of_occurrence
    def test_number_of_occurrence(self):
        test_patterns = [
            (0, [0, 1, 2, 2, 3], 1),
            (4, [0, 1, 2, 2, 3], 0),
            (2, [0, 1, 2, 2, 3], 2),
            (3, [0, 1, 2, 2, 3], 1),
        ]

        for e, s, expected in test_patterns:
            with self.subTest(e=e, s=s, expected=expected):
                self.assertEqual(number_of_occurrence(element=e, sample=s), expected)


if __name__ == "__main__":
    main(verbosity=2)
