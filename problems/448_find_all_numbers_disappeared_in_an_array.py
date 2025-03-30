"""
Basic Approach

- Here the array of n integers contains numbers between 1 to n.
- We need to find out the missing numbers.
- Let's say nums = [1,1,1]
- So length is 3. So here 2 and 3 are missing numbers in range (1,3).
- We can loop through the range (1,n). If number is not present in the set(nums) then we can store it in output list.
- We can return the results.
"""
from typing import List


def findDisappearedNumbers(nums: List[int]):
    result = []
    set_nums = set(nums)
    for i in range(1, len(nums)+1):
        if i not in set_nums:
            result.append(i)
    return result

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    ans = findDisappearedNumbers(nums)
    print(ans)