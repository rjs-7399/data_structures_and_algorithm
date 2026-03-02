"""
Approach:

- Here if we create a set from the given array then it will contain only distinct values.
- Then get the length of set.
- If length of set and initial list both are equal then there are no duplicates.
- If length of set is more than initial list then initial list contains duplicate values.
"""

from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    no_dups = set(nums)
    if len(no_dups) == len(nums):
        return False
    else:
        return True

def main():
    test_1 = [1, 2, 3, 4]
    ans_test_1 = containsDuplicate(test_1)
    print(ans_test_1)
    test_2 = [1, 2, 3, 1]
    ans_test_2 = containsDuplicate(test_2)
    print(ans_test_2)

if __name__ == "__main__":
    main()