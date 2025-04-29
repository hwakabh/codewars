from unittest import TestCase
from unittest import main

from .keep_hydrated import litres


class TestKeepHydrated(TestCase):
    # Test class of keep_hydrated
    def test_litre(self):
        test_patterns = [
            (2, 1),
            (1.4, 0),
            (12.3, 6),
            (0.82, 0),
            (11.8, 5),
            (1787, 893),
            (0, 0),
        ]
        for t, expected in test_patterns:
            with self.subTest(t=t, expected=expected):
                self.assertEqual(litres(time=t), expected)


if __name__ == "__main__":
    main(verbosity=2)
