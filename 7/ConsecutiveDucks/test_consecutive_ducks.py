from unittest import TestCase
from unittest import main

from consecutive_ducks import consecutive_ducks


class TestConsecutiveDucks(TestCase):
    def test_consecutive_ducks(self):
        test_patterns = [
            # Small values testings
            (69, True),
            (8, False),
            (57, True),
            (6, True),
            (13, True),
            (16, False),
            (91, True),
            (75, True),
            (38, True),
            (25, True),
            (32, False),
            (65, True),
            (13, True),
            (16, False),
            (99, True),
            # Medium values testings
            (522, True),
            (974, True),
            (755, True),
            (512, False),
            (739, True),
            (1006, True),
            (838, True),
            (1092, True),
            (727, True),
            (648, True),
            (1024, False),
            (851, True),
            (541, True),
            (1011, True),
            (822, True),
            # Large values testings
            (382131, True),
            (118070, True),
            (17209, True),
            (32768, False),
            (161997, True),
            (400779, True),
            (198331, True),
            (325482, True),
            (88441, True),
            (648, True),
            (65536, False),
            (323744, True),
            (183540, True),
            (65271, True),
            (5263987, True),
        ]
        for x, exp in test_patterns:
            with self.subTest(x=x, exp=exp):
                self.assertEqual(consecutive_ducks(n=x), exp)


if __name__ == "__main__":
    main(verbosity=2)
