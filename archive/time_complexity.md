# Big(O) - Time and Space Complexity

## Time Complexity
- It describes the amount of time necessary to execute an algorithm.

## Space Complexity
- It describes the amount of memory or space utilized by an algorithm.

## Notes
- Both are asymptotic.
- The less time the algorithm takes, the less space it occupies.

## Time Complexity levels

- O(1) - Constant time (flat line)
- O(log n) - Logarithmic time (very slow growth)
- O(n) - Linear time (steady growth)
- O(n²) - Quadratic time (faster growth)
- O(2^n) - Exponential time (very rapid growth)
- O(n!) - Factorial time (extremely rapid growth)


## Big O - Summary

# Time Complexity Reference Table

| Time Complexity | Description                                                                                                                                 | Example                                  |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| O(1)            | Constant - Time taken remains constant regardless of input size                                                                             | Accessing elements in array by index     |
| O(log n)        | Logarithmic - Time taken increases logarithmically as the input grows; operations are typically halved at each step                         | Binary search in sorted array            |
| O(n)            | Linear - Time taken increases proportionately to the size of the input; if N doubles, time taken doubles                                    | Finding an item in unsorted list         |
| O(n log n)      | Linearithmic - Time taken increases in a linearithmic manner; often seen in divide and conquer algorithms                                   | Merge sort or quick sort                 |
| O(n²)           | Quadratic - Time increases quadratically as the input size grows; each element needs to be compared to every other element (nested loops)   | Bubble sort, insertion sort              |
| O(2^n)          | Exponential - Time taken doubles with each addition to N, leading to rapidly growing execution times                                        | Finding all subsets of a set             |
| O(n!)           | Factorial - Time taken increases factorially with each increase in input size, leading to extremely slow execution times                    | Solving the traveling salesman problem   |

