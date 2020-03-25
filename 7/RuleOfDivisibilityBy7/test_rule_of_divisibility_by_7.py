from unittest import TestCase
from unittest import main

from rule_of_divisibility_by_7 import seven


class TestRuleOfDivisibilityBy7(TestCase):
    def test_seven(self):
        ptr = [
            (1603, (7, 2)),
            (371, (35, 1)),
            (483, (42, 1)),
            (1021, (10, 2)),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(seven(m=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
