import sys

x = [1, 2, 3]
print(sys.getrefcount(x))

y = x
print(sys.getrefcount(x))

y = None
print(sys.getrefcount(x))


"""CLI Output
(basevenv) rutvikshah@Rutviks-MacBook-Air pep_coding_functions_and_arrays_level_1 % python3 memory_reference_counting_in_array.py 
2
3
2
"""

"""Explanation
- x is referenced twice initially (once by x, once by getrefcount()).
- Assigning y = x increases the count.
- Setting y = None removes one reference.
"""