from unittest import TestCase

import sympy

from hurwitz_detector.hurwitz import HurwitzCFE
from hurwitz_detector.__init__ import HurwitzCFEDetector
from sympy import SeqFormula, oo, Symbol


class TestHurwitzCFE(TestCase):

    def test_hurwitz_cfedetector(self):
        test_cf = [2, 3, 4, 5, 5, 7, 5, 7, 7, 5, 9, 7]
        test_hurwitz_notation = HurwitzCFEDetector(test_cf, 4)
        sympy.pprint(f"""
        Found HFCE:
            {test_hurwitz_notation}
        for continued fraction:
            {test_cf}
        """)
    def test_hurwitz_cfedetector_2(self):
        test_cf = [2, 5, 1, 5, 8, 1, 12, 11, 1, 19,]
        test_hurwitz_notation = HurwitzCFEDetector(test_cf, 2)
        sympy.pprint(f"""
        Found HFCE:
            {test_hurwitz_notation}
        for continued fraction:
            {test_cf}
        """)
    def test_hurwitz_cfedetector_3(self):
        # test_cf = [5, 3, 2, 2, 1, 1, 16, 1, 2, 2, 5, 2, 3, 1, 28, 1, 4, 2, 8, 2, 5, 1, 40, 1, 6, 2, 11, 2, 7, 1, 52, 1, 8, 2, 14, 2, 9, 1, 64, 1, 10, 2, 17, 2, 11, 1, 76, 1, 12, 2, 20, 2, 13, 1, 88, 1, 14, 2, 23, 2, 15, 1, 100, 1, 16, 2, 26, 2, 17, 1, 112, 1, 18, 2, 29, 2, 19, 1, 124, 1, 20, 2, 32, 2, 21, 1, 136, 1, 22, 2, 35, 2, 23, 1, 148, 1, 24, 2, 38, 2, 25, 1, 160, 1, 26, 2, 41, 2, 27, 1, 172, 1, 28, 2, 44, 2, 29, 1, 184, 1, 30, 2, 47, 2, 31, 1, 196, 1, 32, 2, 50, 2, 33, 1, 208, 1, 34, 2, 53, 2, 35, 1, 220, 1, 36, 2, 56, 2, 37, 1, 232, 1, 38, 2, 59, 2, 39, 1, 244, 1, 40, 2, 62, 2, 41, 1, 256, 1, 42, 2, 65, 2, 43, 1, 268, 1, 44, 2, 68, 2, 45, 1, 280, 1, 46, 2, 71, 2, 47]
        test_cf = [5, 3, 2, 2, 1, 1, 16, 1, 2, 2, 5, 2, 3, 1, 28, 1, 4, 2, 8, 2, 5, 1, 40, 1, 6, 2]
        test_hurwitz_notation = HurwitzCFEDetector(test_cf, 3)
        sympy.pprint(f"""
        Found HFCE:
            {test_hurwitz_notation}
        for continued fraction:
            {test_cf}
        """)

    """
    This case checks an example with a long period. Brought to the attention by Carsten, and has a case where the counters
    need to be incremented earlier than expected
    """
    def test_hurwitz_cfedetector_4(self):
        # Pre-period: 6, 1, 12, 7
        # Main period: 3, 1, 3k+2, 7k-2, 5, 11k-4, 2k+1, 8k+7, 9, 2, k+1, 8k, 3k-2, 1, 1, 4k-1, 3, 14k-13, 8k, 1, 5, 1, 6k-4, 5k-4, 2
        pre_period = [6, 1, 12, 7]
        k = Symbol('k')
        period_seq = SeqFormula((3, 1, 3*k+2, 7*k-2, 5, 11*k-4, 2*k+1, 8*k+7, 9, 2, k+1, 8*k, 3*k-2, 1, 1, 4*k-1, 3, 14*k-13, 8*k, 1, 5, 1, 6*k-4, 5*k-4, 2), (k, 1, oo))
        test_cf = pre_period + list(period_seq[0]) + list(period_seq[1]) + list(period_seq[2])
        test_hurwitz_notation = HurwitzCFEDetector(test_cf, 3)
        print(test_hurwitz_notation)

