from unittest import TestCase
from unittest import main

from .the_wide_mouthed_frog import mouth_size


class TestTheWideMouthedFrog(TestCase):
    def test_mouth_size(self):
        test_patterns = [
            ('toucan', 'wide'),
            ('ant bear', 'wide'),
            ('alligator', 'small'),
        ]
        for n, exp in test_patterns:
            with self.subTest(n=n, exp=exp):
                self.assertEqual(mouth_size(animal=n), exp)


if __name__ == "__main__":
    main(verbosity=2)
