from unittest import TestCase
from unittest import main

from .lottery_machine import lottery


class TestLotteryMachine(TestCase):
    # Test class of lottery_machine
    def test_lottery(self):
        test_patterns = [
            ('wQ8Hy0y5m5oshQPeRCkG', '805'),
            ('ffaQtaRFKeGIIBIcSJtg', 'One more run!'),
        ]
        for i, expected in test_patterns:
            with self.subTest(i=i, expected=expected):
                self.assertEqual(lottery(s=i), expected)


if __name__ == "__main__":
    main(verbosity=2)
