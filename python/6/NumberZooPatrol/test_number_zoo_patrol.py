from unittest import TestCase
from unittest import main

from .number_zoo_partrol import find_missing_number


class TestNumberZooPatrol(TestCase):
    def test_find_missing_number(self):
        ptr = [
            ([2, 3, 4], 1),
            ([1, 3, 4], 2),
            ([1, 2, 4], 3),
            ([1, 2, 3], 4),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(find_missing_number(numbers=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
