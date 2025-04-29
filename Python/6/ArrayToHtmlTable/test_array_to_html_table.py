from unittest import TestCase
from unittest import main

from .array_to_html_table import to_table


class TestArrayToHtmlTable(TestCase):
    def test_to_array(self):
        # Since data of each testcase is tuple, default value would be applied if it does not have.
        # (data:<Array>, header:False, index:False)
        ptr = [
          (
            [["o"]], False, False,
            '<table><tbody><tr><td>o</td></tr></tbody></table>'
          ),
          (
            [["lorem", "ipsum"], ["dolor", "sit amet"]], True, True,
            '<table><thead><tr><th></th><th>lorem</th><th>ipsum</th></tr></thead><tbody><tr><td>1</td><td>dolor</td><td>sit amet</td></tr></tbody></table>'
          ),
          (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], False, True,
            '<table><tbody><tr><td>1</td><td>1</td><td>2</td><td>3</td></tr><tr><td>2</td><td>4</td><td>5</td><td>6</td></tr><tr><td>3</td><td>7</td><td>8</td><td>9</td></tr></tbody></table>'
          ),
          (
            [
              ["id", "name", "price", "quantity"],
              [24351, "pen", 2.41, 500],
              [None, "pencil", 0.99, 25],
              [63401, "grizzly bear", None, 1],
              [3532, "rubber duck", 5.45, 24],
              [1523, None, 3.00, 6.8],
              [11765, "caviar", 67.95, None]
            ], True, False,
            '<table><thead><tr><th>id</th><th>name</th><th>price</th><th>quantity</th></tr></thead><tbody><tr><td>24351</td><td>pen</td><td>2.41</td><td>500</td></tr><tr><td></td><td>pencil</td><td>0.99</td><td>25</td></tr><tr><td>63401</td><td>grizzly bear</td><td></td><td>1</td></tr><tr><td>3532</td><td>rubber duck</td><td>5.45</td><td>24</td></tr><tr><td>1523</td><td></td><td>3.0</td><td>6.8</td></tr><tr><td>11765</td><td>caviar</td><td>67.95</td><td></td></tr></tbody></table>'
          ),
          (
              [["a", "b", "c", "d", "e"], [True, False, False, True, True]], True, False,
              '<table><thead><tr><th>a</th><th>b</th><th>c</th><th>d</th><th>e</th></tr></thead><tbody><tr><td>True</td><td>False</td><td>False</td><td>True</td><td>True</td></tr></tbody></table>'
          )
        ]
        for inp, is_header, is_index, exp in ptr:
            with self.subTest(inp=inp, is_header=is_header, is_index=is_index, exp=exp):
                self.assertEqual(to_table(data=inp, header=is_header, index=is_index), exp)


if __name__ == "__main__":
    main(verbosity=2)
