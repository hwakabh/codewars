# test.assert_equals(tickets([25, 25, 50]), "YES")
# test.assert_equals(tickets([25, 100]), "NO")
# tickets([25, 25, 50, 50, 100]), "NO"

from unittest import TestCase
from unittest import main

from .vasya_clerk import tickets


class TestVasyaClerk(TestCase):
    # Test class of vasya_clerk
    def test_tickets(self):
        test_patterns = [
            ([25, 25, 50], 'YES'),
            ([25, 100], 'NO'),
            ([25, 25, 50, 50, 100], 'NO'),
            ([25, 25], 'YES'),
            # ([25, 25, 50, 50, 50], 'YES') #-> Wrong Case
        ]

        for p, expected in test_patterns:
            with self.subTest(p=p, expected=expected):
                self.assertEqual(tickets(people=p), expected)


if __name__ == "__main__":
    main(verbosity=2)
