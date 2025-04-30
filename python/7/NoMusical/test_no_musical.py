from unittest import TestCase
from unittest import main

from .no_musical import no_musical


class TestNoMusical(TestCase):
    def test_no_musical(self):
        ptr = [
            (2000, 2000, 100, 3, 0),
            (2000, 3000, 0, 50, 1001),
            (2000, 2020, 2, 4, 0),
            (2000, 3000, 5, 2, 600),
        ]
        for s, e, m, d, exp in ptr:
            with self.subTest(s=s, e=e, m=m, d=d, exp=exp):
                self.assertEqual(no_musical(start_class=s, end_class=e, musical_performed_every=m, enrolment_duration=d), exp)


if __name__ == "__main__":
    main(verbosity=2)
