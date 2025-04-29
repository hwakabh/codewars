from unittest import TestCase
from unittest import main

from .rule_of_divisibility_by_13 import thirt


class TestRuleOfDivisibilityBy13(TestCase):
    def test_thirt(self):
        test_patterns = [
            (8529, 79),
            (85299258, 31),
            (5634, 57),
            (1111111111, 71),
            (987654321, 30),
        ]
        for inp, exp in test_patterns:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(thirt(n=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
