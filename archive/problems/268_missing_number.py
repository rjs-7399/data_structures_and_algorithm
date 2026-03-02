"""
Basic Approach:

- Here the array is given [0,1], So length = 2.
- We can loop from 0 to n. If any number is not there then we can return it.

Optimized Approach:

- In mathematics, Formula for sum(n) is as follows:
    S(n) = n*(n+1)/2
- So if len(nums) == 2 then sum must be 3.
- if len(nums) == 3 then sum must be 6.
- if len(nums) == 9 then sum must be 45.
- So what we can do is, first calculate the sum(array) using this formula.
- Then calculate the sum of all digits in the given array.
- Subtract one from another. If the subtraction is zero. Then no missing number.
- Otherwise there is a missing number.
"""


from typing import List

def missingNumber_basic_approach(nums: List[int]):
    for i in range(0, len(nums)+1):
        if i not in nums:
            return i
    return -1

def missingNumber_optimized_approach(nums: List[int]):
    l = len(nums)
    math_sum = (l * (l + 1))//2
    actual_sum = sum(nums)
    return math_sum - actual_sum

def main():
    nums = [9,6,4,2,3,5,7,0,1]
    basic_approach_ans = missingNumber_basic_approach(nums)
    optimized_approach_ans = missingNumber_optimized_approach(nums)

    print(basic_approach_ans)
    print(optimized_approach_ans)

if __name__ == "__main__":
    main()