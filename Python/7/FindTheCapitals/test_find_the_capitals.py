from unittest import TestCase, main

from find_the_capitals import capital


class TestFindTheCapitals(TestCase):
    def test_capital(self):
        ptr = [
            ([{'state': 'Maine', 'capital': 'Augusta'}], ["The capital of Maine is Augusta"]),
            ([{'country': 'Spain', 'capital': 'Madrid'}], ["The capital of Spain is Madrid"]),
            ([{"state" : 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital": "Madrid"}], ["The capital of Maine is Augusta", "The capital of Spain is Madrid"]),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(capital(capitals=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
