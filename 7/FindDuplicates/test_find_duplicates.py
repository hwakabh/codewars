from unittest import TestCase
from unittest import main

from find_duplicates import duplicates


class TestFindDuplicates(TestCase):
    def test_duplicates(self):
        test_patterns = [
            ([1, 2, 4, 4, 3, 3, 1, 5, 3, '5'], [4, 3, 1]),
            ([0, 1, 2, 3, 4, 5], []),
        ]
        for arr, exp in test_patterns:
            with self.subTest(arr=arr, exp=exp):
                self.assertEqual(duplicates(array=arr), exp)


if __name__ == "__main__":
    main(verbosity=2)
