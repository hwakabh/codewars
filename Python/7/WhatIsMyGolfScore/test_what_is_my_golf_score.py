from unittest import TestCase
from unittest import main

from what_is_my_golf_score import golf_score_calculator


class TestWhatIsMyGolfScore(TestCase):
    def test_golf_score_calculator(self):
        # Sample paramters
        par_score = '443454444344544443'
        my_score = '353445334534445344'

        self.assertEqual(golf_score_calculator(par_string=par_score, score_string=my_score), -1)


if __name__ == "__main__":
    main(verbosity=2)
