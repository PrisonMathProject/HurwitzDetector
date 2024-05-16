from unittest import TestCase

from hurwitz_detector.__main__ import HurwitzCFEDetector


class Test(TestCase):
    def test_hurwitz_cfedetector(self):
        test_cf = [2, 3, 4, 5, 5, 7, 5, 7, 7, 5, 9, 7]
        test_hurwitz_notation = HurwitzCFEDetector(test_cf, 2)
