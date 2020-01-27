from unittest import TestCase
from unittest import main

from form_the_largest import max_number


class TestFormTheLargest(TestCase):
    # Test class of form_the_largest
    def test_max_number(self):
        test_patterns = [
            (213, 321),
            (7389, 9873),
            (63792, 97632),
            (63792, 97632),
            (566797, 977665),
            (1000000, 1000000),
            # (13579, 1000000), #-> Wrong Case
        ]

        for number, expected in test_patterns:
            with self.subTest(number=number, expected=expected):
                self.assertEqual(max_number(n=number), expected)


if __name__ == "__main__":
    main(verbosity=2)