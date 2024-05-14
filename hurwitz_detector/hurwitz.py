from typing import Callable, NewType

import sympy

HurwitzPeriodFunction = NewType("HurwitzPeriodFunction", sympy.Function)
class HurwitzCFE:
    def __init__(self, pre_period: [int], period_funcs: [HurwitzPeriodFunction]):
        self.pre_period = pre_period
        self.period = period_funcs

    def __str__(self):
        periodic_funcs = ', '.join(map(str, self.period))
        return "[" + ', '.join(map(str,self.pre_period)) + ", " + periodic_funcs + sympy.Symbol("]_k=1^{(oo)}").__str__()
