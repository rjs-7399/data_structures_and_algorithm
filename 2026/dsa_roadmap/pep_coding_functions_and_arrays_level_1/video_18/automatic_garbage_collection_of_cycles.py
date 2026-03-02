import gc
print(gc.get_threshold())

"""CLI Output
(basevenv) rutvikshah@Rutviks-MacBook-Air pep_coding_functions_and_arrays_level_1 % python3 automatic_garbage_collection_of_cycles.py 
(2000, 10, 10)
"""

"""Explanation
- It returns the threshold tuple for generation 0,1 and 2.
- When allocations exceed the threshold, collection is triggered.
"""