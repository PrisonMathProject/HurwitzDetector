from typing import Callable, NewType

import sympy

HurwitzPeriodFunction = NewType("HurwitzPeriodFunction", sympy.Function)
class HurwitzCFE:
    def __init__(self, pre_period: [int], period_funcs: [HurwitzPeriodFunction]):
        self.pre_period = pre_period
        self.period = period_funcs

    def __str__(self):
        periodic_funcs = ', '.join(map(str, self.period))
        return "[" + ', '.join(map(str,self.pre_period)) + ", \overline{" + periodic_funcs + "}" + sympy.Symbol("]_{k=1}{\infty}").__str__()

    def matches(self, reg_cont_fraction: list[int]) -> bool:
        simplified_cfe = self.simplify(len(reg_cont_fraction))
        return simplified_cfe == reg_cont_fraction
    def simplify(self, length: int) -> list[int]:
        """
        Simplifies the continued fraction to a list of values for length len
        :param len: The length to simplify the continued fraction to
        :return:
        """
        ret_val = list()
        k_val = 0
        for i in range(length):
            if i < len(self.pre_period):
                ret_val.append(self.pre_period[i])
            else:
                period_index = (i - len(self.pre_period)) % len(self.period)
                i_pos_func = self.period[period_index]
                # We increment k once for every period
                if period_index == 0:
                    k_val += 1
                k = sympy.Symbol("k")
                period_val = i_pos_func.subs(k, k_val)
                ret_val.append(period_val)
        return ret_val
