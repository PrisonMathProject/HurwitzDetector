from itertools import groupby


def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)
def all_equal_not_none(iterable):
    return all(iterable) and all_equal(iterable)
