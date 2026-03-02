"""
Basic Approach


- itr 1:
map = {}
    diff = 9-2 = 7
    if diff in map: no
    map[2] = 0

- itr 2:
map = {2:1}
    diff = 9-11 = -2
    if diff in map: no
    map[11] = 1

- itr 3:
map = {2:1, 11:1}
    diff = 9-11 = -8
    if diff in map: no
    map[15] = 2

- itr 4:
map = {2:1, 11:1, 15:2}
    diff = 9-7 = 2
    if diff in map: yes
    return [3, 0]


- Array = [2, 11, 15, 7]
- Here the array is give. We need to find out the indices which can make a sum equal to target number.
- Here we can loop through the given array.
- for each index subtract nums[i] from target. If target - nums[i] is present in array then return its index and i.
"""
from typing import List

def twoSum(target, nums: List[int]):
    for i in range(0, len(nums)):
        carry = target - nums[i]
        if carry in nums:
            carry_index = nums.index(carry)
            if i != carry_index:
                return [i, carry_index]
    return []

def twoSumHashMap(target, nums: List[int]):
    map = {}
    for index,value in enumerate(nums):
        diff = target - value
        if diff in map:
            return [index, map[diff]]
        map[value] = index
    return []

if __name__ == "__main__":
    nums = [2, 11, 15, 7]
    target = 9
    ans_1 = twoSum(target, nums)
    ans_2 = twoSumHashMap(target, nums)
    print(ans_1)
    print(ans_2)
