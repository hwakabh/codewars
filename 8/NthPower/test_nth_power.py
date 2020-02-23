from unittest import TestCase
from unittest import main

from nth_power import index


class TestNthPower(TestCase):
    def test_index(self):
        test_patterns = [
            ([1, 2, 3, 4], 2, 9),
            ([1, 3, 10, 100], 3, 1000000),
        ]
        for arr, n, exp in test_patterns:
            with self.subTest(arr=arr, n=n, exp=exp):
                self.assertEqual(index(array=arr, n=n), exp)


if __name__ == "__main__":
    main(verbosity=2)
