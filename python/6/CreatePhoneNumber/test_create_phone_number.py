from unittest import TestCase
from unittest import main

from .create_phone_number import create_phone_number


class TestCreatePhoneNumber(TestCase):
    # Test class of create_phone_number
    def test_create_phone_number(self):
        test_patterns = [
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], '(123) 456-7890'),
            ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], '(111) 111-1111'),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], '(123) 456-7890'),
            ([0, 2, 3, 0, 5, 6, 0, 8, 9, 0], '(023) 056-0890'),
            ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], '(000) 000-0000'),
            # ([0, 9, 0, 9, 6, 7, 5, 8, 1, 3], '(090) 967-5811'), #-> Wrong Case
        ]

        for nums, expected in test_patterns:
            with self.subTest(nums=nums, expected=expected):
                self.assertEqual(create_phone_number(n=nums), expected)


if __name__ == '__main__':
    main(verbosity=2)
