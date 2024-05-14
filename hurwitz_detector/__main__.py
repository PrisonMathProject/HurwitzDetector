from typing import NewType, Callable, Optional

import sympy

from hurwitz_detector import hurwitz
from hurwitz_detector.util import all_equal

HurwitzPeriodicChecker = NewType("HurwitzPeriodicChecker", Callable[[int, int], list[int]])


def build_period_val(reg_cont_fraction: [int], g: int, h: int, u: int) -> Optional[hurwitz.HurwitzPeriodFunction]:
    a = reg_cont_fraction[g-h+u-1]
    b = reg_cont_fraction[g+u-1]
    c = reg_cont_fraction[g+h+u-1]
    if a == b == c:
        return sympy.Symbol(a)
    elif a < b < c:
        k = sympy.Symbol("k")
        return sympy.simplify((b-a)*k + 2*a - b)
    else:
        return None


def HurwitzCFEDetector(reg_cont_fraction: [int], periodic_checker_count: int) -> Optional[hurwitz.HurwitzCFE]:
    for g in range(1, len(reg_cont_fraction)):
        for h in range(1, g+1): #h <= g
            periodic_checker_seqs = build_periodic_checker_seq(periodic_checker_count)
            sequences_match = all_equal([periodic_checker_seq(g, h) for periodic_checker_seq in periodic_checker_seqs])
            if sequences_match:
                # We know the period starts at h
                pre_period = reg_cont_fraction[0:h]
                period_funcs = [build_period_val(reg_cont_fraction, g, h, u) for u in range(1, h+1)]
                return hurwitz.HurwitzCFE(pre_period, period_funcs)
    return None

def build_periodic_checker_seq(periodic_checker_count: int) -> [HurwitzPeriodicChecker]:
    """
    Constructs a number of periodic checker functions, based on the desired amount passed in.
    These will be used to check for a period within the continued fraction.
    :param periodic_checker_count: Number of periodic checker functions to create
    :return:
    """
    pass