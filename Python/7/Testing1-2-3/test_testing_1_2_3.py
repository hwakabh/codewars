from unittest import TestCase
from unittest import main

from .testing_1_2_3 import number


class TestTesting123(TestCase):
    def test_number(self):
        test_patterns = [
            ([], []),
            (['a', 'b', 'c'], ['1: a', '2: b', '3: c']),
            (['', 'b', '', '', ''], ['1: ', '2: b', '3: ', '4: ', '5: ']),
        ]
        for inp, exp in test_patterns:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(number(lines=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
