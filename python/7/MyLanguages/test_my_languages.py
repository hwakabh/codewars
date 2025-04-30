from unittest import TestCase
from unittest import main

from .my_languages import my_languages


class TestMyLanguages(TestCase):
    def test_my_languages(self):
        ptr = [
            ({'Java': 10, 'Ruby': 80, 'Python': 65}, ['Ruby', 'Python']),
            ({'Hindi': 60, 'Dutch': 93, 'Greek': 71}, ['Dutch', 'Greek', 'Hindi']),
            ({'C++': 50, 'ASM': 10, 'Haskell': 20}, []),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(my_languages(results=inp), exp)


if __name__ == '__main__':
    main(verbosity=2)
