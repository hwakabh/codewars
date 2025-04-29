from unittest import TestCase
from unittest import main

from .unary_function_chainer import chained


class TestUnaryFunctionChainer(TestCase):
    def test_unary_function_chainer(self):
        def f1(x): return x * 2
        def f2(x): return x + 2
        def f3(x): return x ** 2
        self.assertEqual(chained(functions=[f1,f2,f3], v=0), 4)
        self.assertEqual(chained(functions=[f1,f2,f3], v=2), 36)
        self.assertEqual(chained(functions=[f3,f2,f1], v=2), 12)

        def f4(x): return x.split()
        def f5(xs): return [x[::-1].title() for x in xs]
        def f6(xs): return "_".join(xs)
        self.assertEqual(chained(functions=[f4,f5,f6], v="lorem ipsum dolor"), "Merol_Muspi_Rolod")


if __name__ == "__main__":
    main(verbosity=2)
