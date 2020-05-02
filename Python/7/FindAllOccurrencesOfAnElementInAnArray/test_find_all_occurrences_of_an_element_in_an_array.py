from unittest import TestCase
from unittest import main

from find_all_occurrences_of_an_element_in_an_array import find_all


class TestFindAllOccurrencesOfAnElementInAnArray(TestCase):
    def test_find_all(self):
        ptr = [
            ([6, 9, 3, 4, 3, 82, 11], 3, [2, 4]),
            ([10, 16, 20, 6, 14, 11, 20, 2, 17, 16, 14], 16, [1, 9]),
            ([20, 20, 10, 13, 15, 2, 7, 2, 20, 3, 18, 2, 3, 2, 16, 10, 9, 9, 7, 5, 15, 5], 20, [0, 1, 8]),
        ]
        for inp, k, exp in ptr:
            with self.subTest(inp=inp, k=k, exp=exp):
                self.assertEqual(find_all(array=inp, n=k), exp)


if __name__ == "__main__":
    main(verbosity=2)
