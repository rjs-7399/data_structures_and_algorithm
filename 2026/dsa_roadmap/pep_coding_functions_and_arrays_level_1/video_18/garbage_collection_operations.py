import gc

gc.collect()

gc.enable()

gc.disable()

"""Explanation
- gc.collect() forces garbage collection to free memory by cleaning up unreferenced objects.
- gc.enable() re-enables automatic garbage collection.
- gc.disable() disables automatic garbage collection.
"""