from unittest import TestCase
from unittest import main

from substring_fun import nth_char


class TestSubstringFun(TestCase):
    def test_nth_char(self):
        test_pattern = [
            (['yoda', 'best', 'has'], 'yes'),
            ([], ''),
            (['X-ray'], 'X'),
            (['No', 'No'], 'No'),
            (['Chad', 'Morocco', 'India', 'Algeria', 'Botswana', 'Bahamas', 'Ecuador', 'Micronesia'], 'Codewars'),
        ]
        for inp, exp in test_pattern:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(nth_char(words=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
