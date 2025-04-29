from unittest import TestCase
from unittest import main

from .persistence_bugger import persistence


class TestPersistenceBugger(TestCase):
    def test_persistence(self):
        test_patterns = [
            (39, 3),
            (4, 0),
            (25, 2),
            (999, 4),
        ]
        for inp, exp in test_patterns:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(persistence(n=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
