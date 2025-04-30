from unittest import TestCase
from unittest import main

from .count_the_monkyes import monkey_count


class TestCountTheMonkeys(TestCase):
    def test_monkey_count(self):
        test_patterns = [
            (5, [1, 2, 3, 4, 5]),
            (3, [1, 2, 3]),
            (9, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
            (10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            (20, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
        ]
        for inp, exp in test_patterns:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(monkey_count(n=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
