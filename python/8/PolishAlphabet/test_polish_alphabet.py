from unittest import TestCase
from unittest import main

from .polish_alphabet import correct_polish_letters


class TestPolishAlphabet(TestCase):
    def test_correct_polish_letters(self):
        ptr = [
            ('Jędrzej Błądziński', 'Jedrzej Bladzinski'),
            ('Lech Wałęsa', 'Lech Walesa'),
            ('Maria Skłodowska-Curie', 'Maria Sklodowska-Curie'),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(correct_polish_letters(st=inp), exp)


if __name__ == '__main__':
    main(verbosity=2)
