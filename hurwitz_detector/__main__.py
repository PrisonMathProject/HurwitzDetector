import sys

import sympy

from hurwitz_detector import HurwitzCFEDetector

input_args = sys.argv[1:]
fraction_segment = list2 = [int(c) for c in input_args[0].split(',')]
search_func_numb = int(input_args[1]) if len(input_args) > 1 else 2
print(
    f"Calculating Hurwitz Notation for fraction segment {fraction_segment} with {search_func_numb} periodic search functions...")
hurwitz_notation = HurwitzCFEDetector(fraction_segment, search_func_numb)
sympy.pprint(f"""
        Found HFCE:
            {hurwitz_notation}
        for continued fraction:
            {fraction_segment}
        """)
