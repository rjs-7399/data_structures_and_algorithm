"""
[1,1]
[2,2]
[3,3]
[3,4]
[2,3]
[1,2]
[0,1]
[-1,0]

Basic Approach

- Here we can move horizontally, diagonally or vertically.
- Here at each step we consider it as a total seconds to reach to the end vertex.
- Here we can also calculate like below.

- [[1,1], [3,4], [-1,0]]
- so at first iteration: from [1,1] to [3,4], we can do this: [3,4] - [1,1] = [2,3]
- so in the second iteration: from [3,4] to [-1,0], we can do this: [-1,0] - [3,4] = [-4, -4]
- Now [2,3] - [-4,-4] = [6,7]
- Now bigger number = 7.
- So total it will take 7 seconds.
"""
from typing import List
def minTimeToVisitAllPoints(points: List[List[int]]):
    result = 0
    x1,y1 = points.pop(0)
    while points:
        x2, y2 = points.pop(0)
        result += max(abs(x2-x1), abs(y2-y1))
        x1,y1 = x2,y2
    return result

if __name__ == "__main__":
    points = [[3,2],[-2,2]]
    ans = minTimeToVisitAllPoints(points)
    print(ans)