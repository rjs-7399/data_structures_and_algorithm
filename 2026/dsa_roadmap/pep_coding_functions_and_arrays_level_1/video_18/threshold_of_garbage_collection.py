import gc

gc.set_threshold(500, 5, 5)

t = gc.get_threshold()
print(t)

"""CLI Output
(basevenv) rutvikshah@Rutviks-MacBook-Air pep_coding_functions_and_arrays_level_1 % python3 threshold_of_garbage_collection.py               
(500, 5, 5)
"""