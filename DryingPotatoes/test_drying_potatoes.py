from unittest import TestCase
from unittest import main

from drying_potatoes import potatoes


class TestDryingPotatoes(TestCase):
    def test_potatoes(self):
        test_patterns = [
            (82, 127, 80, 114),
            (93, 129, 91, 100),
        ]
        for p0, w0, p1, exp in test_patterns:
            with self.subTest(p0=p0, w0=w0, p1=p1, exp=exp):
                self.assertEqual(potatoes(p0=p0, w0=w0, p1=p1), exp)


if __name__ == "__main__":
    main(verbosity=2)
