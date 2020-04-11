from unittest import TestCase
from unittest import main

from is_the_string_uppercase import is_uppercase


class TestIsTheStringUppercase(TestCase):
    def test_is_upper(self):
        ptr = [
            ('c', False),
            ('C', True),
            ('hello I AM DONALD', False),
            ('HELLO I AM DONALD', True),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(is_uppercase(inp=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
