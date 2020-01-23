from unittest import TestCase
from unittest import main

from friends_or_foe import friends


class TestFriendsOrFoe(TestCase):
    # Test class of friends_or_foe
    def test_friends(self):
        test_patterns = [
            (['Ryan', 'Kieran', 'Mark'], ['Ryan', 'Mark']),
            (['Ryan', 'Kieran', 'Jason', 'Yous'], ['Ryan', 'Yous']),
        ]

        for f, expected in test_patterns:
            with self.subTest(f=f, expected=expected):
                self.assertEqual(friends(x=f), expected)


if __name__ == "__main__":
    main(verbosity=2)