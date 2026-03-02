import gc

def func(i):
    x = {}
    x[i+1] = x
    return x

c = gc.collect()
print(c)

for i in range(10):
    func(i)

c = gc.collect()
print(c)


"""CLI Output
(basevenv) rutvikshah@Rutviks-MacBook-Air pep_coding_functions_and_arrays_level_1 % python3 manual_garbage_collection.py 
12
10
"""

"""Explanation
- def fun(i) creates a cyclic reference by making a dictionary reference itself.
- gc.collect() triggers garbage collection and stores the count of collected objects.
- for i in range(10 calls fun(i) 10 times, creating 10 cyclic references.
- gc.collect() triggers garbage collection again and prints the count of collected objects.
"""