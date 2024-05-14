from unittest import TestCase

import sympy

from hurwitz_detector.hurwitz import HurwitzCFE


class TestHurwitzCFE(TestCase):

    def test_str(self):
        test_hurwitz = HurwitzCFE([1, 2, 3], [sympy.Symbol("5"), sympy.Function('2k+3'), sympy.Function('7')])

