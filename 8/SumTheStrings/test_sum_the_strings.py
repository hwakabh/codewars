from unittest import TestCase
from unittest import main

from sum_the_strings import sum_str


class TestSumTheStrings(TestCase):
    def test_sum_str(self):
        test_patterns = [
            ('4', '5', '9'),
            ('34', '5', '39'),
        ]
        for x, y, exp in test_patterns:
            with self.subTest(x=x, y=y, exp=exp):
                self.assertEqual(sum_str(a=x, b=y), exp)


if __name__ == '__main__':
    main(verbosity=2)
