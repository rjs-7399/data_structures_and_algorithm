"""
1 2 3
4 5 6
7 8 9

- Here the correct answer will be [1,2,3,6,9,8,7,4,5].
- Here we can add two conditions. We need to move in slice.
- So first we will traverse first row from left to right only.
- Once the boundary hits, we will change the direction and traverse the last column only.
- Once the boundary hits, we will change the direction and traverse the last row from right to left.
- Once the boundary hits, we will change the direction from bottom to top.
- At last we will traverse middle row from left to right.
"""