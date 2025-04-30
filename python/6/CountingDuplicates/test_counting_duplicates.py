from unittest import TestCase
from unittest import main

from .counting_duplicates import duplicate_count


class TestCountingDuplicates(TestCase):
    def test_duplicate_count(self):
        ptr = [
            ('abcde', 0),
            ('abcdea', 1),
            ('indivisibility', 1),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(duplicate_count(text=inp), exp)


if __name__ == '__main__':
    main(verbosity=2)
