from unittest import TestCase
from unittest import main

from .no_zeros_for_heros import no_boring_zeros


class TestNoZerosForHeros(TestCase):
    def test_no_boring_zeros(self):
        test_patterns = [
            (1450, 145),
            (960000, 96),
            (1050, 105),
            (-1050, -105),
            (0, 0),
        ]
        for num, exp in test_patterns:
            with self.subTest(num=num, exp=exp):
                self.assertEqual(no_boring_zeros(n=num), exp)


if __name__ == "__main__":
    main(verbosity=2)
