from unittest import TestCase
from unittest import main

from grasshopper import goals


class TestGrasshopper(TestCase):
    # Test class of grasshopper
    def test_goals(self):
        test_patterns = [
            (0, 0, 0, 0),
            (5, 10, 2, 17),
        ]
        for liga, copa, cl, expected in test_patterns:
            with self.subTest(liga=liga, copa=copa, cl=cl, expected=expected):
                self.assertEqual(goals(laLiga=liga, copaDelRey=copa, championsLeague=cl), expected)


if __name__ == "__main__":
  main(verbosity=2)