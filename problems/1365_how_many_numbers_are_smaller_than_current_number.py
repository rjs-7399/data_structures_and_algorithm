"""
Basic Approach

nums = [8, 1, 2, 2, 3]

- here the array of n numbers is given. We have to find count of smaller numbers then current one.
- First we need to sort the array.
- [1, 2, 2, 3, 8]
- Now we will loop through the array and store number as key and its index as value.
- With this approach, index represents exact position of given integer in sorted order.
- Here if the number is repeated then we won't store its key value to the map.
- {1:0, 2:1, 3:3, 8:4}
- Now we simply loop through origin nums again and will print the index from hashmap.
- [4,0,1,1,3]
"""

from typing import List

def smallerNumbersThanCurrent(nums: List[int]):
    map = {}
    nums1 = [] + nums
    nums.sort()
    result = []
    for index,value in enumerate(nums):
        if value not in map:
            map[value] = index
    for element in nums1:
        result.append(map[element])
    return result

if __name__ == "__main__":
    nums = [7,7,7,7]
    ans = smallerNumbersThanCurrent(nums)
    print(ans)