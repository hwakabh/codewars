from unittest import TestCase
from unittest import main

from .greet_me import greet


class TestGreetMe(TestCase):
    def test_greet(self):
        ptr = [
            ('riley', 'Hello Riley!'),
            ('molly', 'Hello Molly!'),
            ('BILLY', 'Hello Billy!'),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(greet(name=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
