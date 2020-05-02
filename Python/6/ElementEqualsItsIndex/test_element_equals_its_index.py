from unittest import TestCase
from unittest import main

from element_equals_its_index import index_equals_value


class TestElementEqualsItsIndex(TestCase):
    def test_index_equals_value(self):
        test_patterns = [
            ([-8, 0, 2, 5], 2),
            ([-1, 0, 3, 6], -1),
            ([-3, 0, 1, 3, 10], 3),
            ([-5, 1, 2, 3, 4, 5, 7, 10, 15], 1),
            ([9, 10, 11, 12, 13, 14], -1),
            ([0,], 0),
        ]
        for inp, exp in test_patterns:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(index_equals_value(arr=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
