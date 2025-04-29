from unittest import TestCase
from unittest import main

from .numbers_to_letters import switcher


class TestNumbersToLetters(TestCase):
    def test_switcher(self):
        ptr = [
            (['24', '12', '23', '22', '4', '26', '9', '8'], 'codewars'),
            (['25','7','8','4','14','23','8','25','23','29','16','16','4'], 'btswmdsbd kkw'),
            (['4', '24'], 'wc'),
            (['12'], 'o'),
            (['12','28','25','21','25','7','11','22','15'], 'o?bfbtpel'),
        ]

        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(switcher(arr=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
