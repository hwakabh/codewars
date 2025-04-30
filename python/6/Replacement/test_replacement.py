from unittest import TestCase
from unittest import main

from .replacement import sort_number


class TestReplacement(TestCase):
    def test_sort_number(self):
        ptr = [
            ([1,2,3,4,5], [1,1,2,3,4]),
            ([4,2,1,3,5], [1,1,2,3,4]),
            ([2,3,4,5,6], [1,2,3,4,5]),
            ([2,2,2], [1,2,2]),
            ([42], [1]),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(sort_number(a=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
