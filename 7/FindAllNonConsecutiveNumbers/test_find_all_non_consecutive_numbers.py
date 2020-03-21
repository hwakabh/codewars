from unittest import TestCase
from unittest import main

from find_all_non_consecutive_numbers import all_non_consecutive


class TestFindAllNonConsecutiveNumbers(TestCase):
    def test_all_non_consecutive(self):
        inp = [1, 2, 3, 4, 6, 7, 8, 10]
        exp = [{'i': 4, 'n': 6}, {'i': 7, 'n': 10}]
        self.assertEqual(all_non_consecutive(arr=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
