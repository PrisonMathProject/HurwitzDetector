from typing import NewType, Callable, Optional

import sympy

from hurwitz_detector import hurwitz
from hurwitz_detector.util import all_equal_not_none

# Represents a sequence of functions that generates a sequence that is used to check for a period
# (ag+(μ−1)h+ν − ag+(μ−2)h+ν)_v=0^{(h−1)}
HurwitzPeriodSeqGenerator = NewType("HurwitzPeriodSeqGenerator", Callable[[list[int], int, int], list[int]])

def print_period_seqs(g, h, period_seqs):
    period_seqs_txt = ", ".join(map(str, period_seqs))
    sympy.pprint(f"Periodic Checker Sequences for {(g, h)}: {period_seqs_txt}")


def HurwitzCFEDetector(reg_cont_fraction: [int], periodic_checker_count: int) -> Optional[hurwitz.HurwitzCFE]:
    # in order to avoid an index-of-bounds error, we need to ensure
    g_upper_bound = len(reg_cont_fraction)
    for g in range(1, g_upper_bound):
        for h in range(1, g+1): #h <= g
            periodic_checker_seqs = build_periodic_checker_seqs(g, h, len(reg_cont_fraction), periodic_checker_count)
            period_seqs = list(map(lambda x: x(reg_cont_fraction, g, h), periodic_checker_seqs))
            print_period_seqs(g, h, period_seqs)
            sequences_match = all_equal_not_none(period_seqs)
            if sequences_match:
                # We know the period starts at h
                pre_period = reg_cont_fraction[0:g-h]
                period_funcs: list[Optional[hurwitz.HurwitzPeriodFunction]] = [build_period_val(reg_cont_fraction, g, h, u) for u in range(1, h+1)]
                # If Any of the period functions are None, we need to move to the next h
                if None not in period_funcs:
                    potential_hcfe = hurwitz.HurwitzCFE(pre_period, period_funcs)
                    # Check the hcfe matches the values of the continued fraction
                    if potential_hcfe.matches(reg_cont_fraction):
                        return potential_hcfe
    return None


def build_period_val(reg_cont_fraction: [int], g: int, h: int, u: int) -> Optional[hurwitz.HurwitzPeriodFunction]:
    a = reg_cont_fraction[g-h+u-1]
    b = reg_cont_fraction[g+u-1]
    c = reg_cont_fraction[g+h+u-1]
    if a == b == c:
        return sympy.simplify(a)
    elif a < b < c:
        k = sympy.Symbol("k")
        return sympy.simplify((b-a)*k + 2*a - b)
    else:
        """
        This is the "otherwise" case from 38b, we need to move to the next h
        """
        return None


def build_periodic_checker_seqs(g: int, h: int, cont_fac_length: int, periodic_checker_count: int) -> [HurwitzPeriodSeqGenerator]:
    """
    Constructs a number of periodic checker functions, based on the desired amount passed in.
    These will be used to check for a period within the continued fraction. Cannot use LESS than
    2 sequences.
    :param periodic_checker_count: Number of periodic checker functions to create
    :return:
    """
    # The periodic checker count must be at least 2, but, to prevent an index out of bounds,
    # we must adjust the number, if too many are requested, vs. the length of the continued fraction
    N = cont_fac_length
    search_func_index_limit = max(2, ((-g+h+N+1)//h)-1)
    if periodic_checker_count > search_func_index_limit:
        print(f"Search Function count adjusted to prevent index out of bounds. Capped at {search_func_index_limit}")
    periodic_checker_count = min(max(2, periodic_checker_count), search_func_index_limit)
    ret_val = list()
    for i in range(1, periodic_checker_count+1):
        ret_val.append(build_periodic_checker_seq(i))
    return ret_val


def build_periodic_checker_seq(u: int) -> HurwitzPeriodSeqGenerator:
    """
    (a_g+(μ−1)h+ν − a_g+(μ−2)h+ν)_v=0^{(h−1)}
    μ = seq_index
    :param u:
    :return:
    """
    return lambda a, g, h: search_func(a, g, h, u)


def search_func(a: [int], g: int, h: int, u: int) -> Optional[list[int]]:
    if g + (u - 1)*h + h-1 < len(a):
        return [a[g + (u - 1)*h + v] - a[g + (u-2)*h + v] for v in range(h)]
    else:
        return None
