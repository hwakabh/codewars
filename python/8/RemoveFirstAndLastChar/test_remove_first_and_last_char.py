from unittest import TestCase
from unittest import main

from .remove_first_and_last_char import remove_char


class TestRemoveFirstAndLastChar(TestCase):
    # Test class of remove_first_and_last_char
    def test_remove_char(self):
        test_patterns = [
            ('eloquent', 'loquen'),
            ('country', 'ountr'),
            ('person', 'erso'),
            ('place', 'lac'),
            ('ok', ''),
            # ('bug', 'ug'),  #-> Wrong Case
        ]

        for w, expected in test_patterns:
            with self.subTest(w=w, expected=expected):
                self.assertEqual(remove_char(s=w), expected)


if __name__ == "__main__":
    main(verbosity=2)
