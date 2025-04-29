from unittest import TestCase
from unittest import main

from .count_letters_and_digits import count_letters_and_digits


class TetstCountLettersAndDigits(TestCase):
    # Test class of count_letters_and_digits
    def test_count_letters_and_digits(self):
        test_patterns = [
            ('n!!ice!!123', 7),
            ('de?=?=tttes!!t', 8),
            ('', 0),
            ('!@#$%^&`~.', 0),
            ('u_n_d_e_r__S_C_O_R_E', 10)
        ]
        for s, expected in test_patterns:
            with self.subTest(s=s, expected=expected):
                self.assertEqual(count_letters_and_digits(s=s), expected)


if __name__ == "__main__":
    main(verbosity=2)
