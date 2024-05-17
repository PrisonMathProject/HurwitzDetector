from unittest import TestCase

import sympy

from hurwitz_detector.__main__ import HurwitzCFEDetector


class Test(TestCase):
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
