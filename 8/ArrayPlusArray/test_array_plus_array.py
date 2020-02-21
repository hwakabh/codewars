from unittest import TestCase
from unittest import main

from array_plus_array import array_plus_array


class TestArrayPlusArray(TestCase):
    def test_array_plus_array(self):
        test_patterns = [
            ([1, 2, 3], [4, 5, 6], 21),
            ([-1, -2, -3], [-4, -5, -6], -21),
            ([0, 0, 0], [4, 5, 6], 15),
            ([100, 200, 300], [400, 500, 600], 2100),
        ]
        for x, y, expected in test_patterns:
            with self.subTest(x=x, y=y, expected=expected):
                self.assertEqual(array_plus_array(arr1=x, arr2=y), expected)


if __name__ == "__main__":
    main(verbosity=2)
