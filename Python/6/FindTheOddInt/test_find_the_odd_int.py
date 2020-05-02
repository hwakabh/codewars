from unittest import TestCase
from unittest import main

from find_the_odd_int import find_it


class TestFindTheOddInt(TestCase):
    def test_find_it(self):
        test_patterns = [
            ([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5], 5),
            ([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5], -1), 
            ([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5], 5),
            ([10], 10),
            ([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1], 10),
            ([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10], 1),
        ]
        for a, expected in test_patterns:
            with self.subTest(a=a, expected=expected):
                self.assertEqual(find_it(seq=a), expected)


if __name__ == '__main__':
    main(verbosity=2)

