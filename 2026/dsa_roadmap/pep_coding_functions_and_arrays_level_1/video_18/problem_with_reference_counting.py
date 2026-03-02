import sys

x = [1, 2, 3]
y = [4, 5, 6]

x.append(y)
y.append(x)

print(sys.getrefcount(x))
print(sys.getrefcount(y))

"""CLI Output
(basevenv) rutvikshah@Rutviks-MacBook-Air pep_coding_functions_and_arrays_level_1 % python3 problem_with_reference_counting.py 
3
3
"""

"""Explanation
- x contains y and y contains x.
- Even after deleting x and y. Python won't be able to free the memory just using reference counting, because each still reference the other.
"""
