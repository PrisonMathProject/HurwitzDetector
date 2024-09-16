# Hurwitz Fraction Detector Algorithm

Algorithm Implementation found in [__init__.py](../src/hurwitz/__init__.py)

## Algorithm Psuedocode

*Assume lists are 0-indexed*

```psuedocode
define the fraction_array as a list of elements of a regular continued fraction expansion
define the period_checker_func_count as the number of sequences to use to detect a period. This value cannot be less than 2. 

define function detector(fraction, period_checker_func_count)
    define the upper_bound as the last index of the fraction_array
    For g = 1 <= upper_bound
        For h = 1 <= g
            define sequence_values as the return of the call sequence_values_builder(fraction_array, g, h, period_checker_func_count) 
            If sequence_values are equal
                define the pre_period as the sub-list of fraction_array from 0 to g-h
                define period_func as the return of the call period_funcs_builder(fraction_array, g, h)
                If period_func is valid
                    return the Hurwitz fraction defined as the pre_period + period_func
                Else
                    continue on to the next iteration of the loops
            Else
                continue on to the next iteration of the loops
            
define function sequence_values_builder(fraction_array, g, h, period_checker_func_count)
    define the upper_bound as the last index of the fraction_array
    # The sequence_limit is defined to ensure we do not create a sequence that goes out of the bounds of the fraction_array. 
    # Please note the use of the floor-division symbol in the equation 
    define the sequence_limit as the bigger value of (2 and ((-g+h+N+1)//h)-1)
    define sequence_list as an empty list that will be built below
    For u = 1 <= smaller value of (period_checker_func_count, sequence_limit)
        define sequence as S_u(g,h) := (a_{g+(u-1)h}-a_{g+(u-2)h},...,a_{g+uh-1}-a_{g+(u-1)(h-1)})
        add sequence to sequence_list
    define return_value as the list of evaluations of the sequence_lists using the fraction_array
    return return_value     
    
define function period_funcs_builder(fraction_array, g, h)
    define return_value as an empty list that will be returned
    For u = 1 <= h
        define a as g-h+u-1
        define b as g+u-1
        define c as g+h+u-1
        If the elements of fraction_array at positions a,b, and c are equal
            add the element of fraction_array at position a to return_value
        Else If
            add an element defined by the mathematical expression ((b-a)k + 2*a - b) to return_value 
        Else
            return Invalid and exit the function
    return return_value
```