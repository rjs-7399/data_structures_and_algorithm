"""
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

- Here we run a for loop to traverse through all the index of the grid and maintain the list called visited nodes.
- If the node is already visited then we append it to the visited list.
- For each index we apply BFS.
- Inside BFS, for a given index we check all the 4 neighbour index and check they are 1 or not and they are visited or not.
- If they are 1, and they are not visited then add that to dequeue and visited both.
- We keep repeating this step till queue is not empty. For a given node. And then we go back to the for loop.

Dry Run:


Iteration 1:
- In main:
- grid[0][0] == "1" and not in visit:
    - Start BFS(0,0)
    - In BFS:
        - visit = [(0,0)]
        - queue = [(0,0)]
        - Inside loop:
        - Iteration 1: (0,1)
            - r,c = (0,0) + (0,1) = (0,1)
            - queue = [(0,1)]
            - visit = [(0,1)]
        - Iteration 2: (0,-1)
            - r,c = (0,0) + (0,-1) = (0,-1)
            - condition not satisfied
        - Iteration 3: (1,0)
            - r,c = (0,0) + (1,0) = (1,0)
            - queue = [(0,1), (1,0)]
            - visit = [(0,1), (1,0)]
        - Iteration 4: (-1,0)
            - r,c = (0,0) + (-1,0) = (-1,0)
            - condition not satisfied

        - visit = [(0,1), (1,0)]
        - queue = [(0,1), (1,0)]
        - Now queue.popleft = (0,1)
        - Inside loop:
        - Iteration 1: (0,1)
            - r,c = (0,1) + (0,1) = (0,2)
            - queue = [(1,0), (0,2)]
            - visit = [(0,1), (1,0), (0,2)]
        - Iteration 2: (0,-1)
            - r,c = (0,1) + (0,-1) = (0,0)
            - already visited
        - Iteration 3: (1,0)
            - r,c = (0,1) + (1,0) = (1,1)
            - queue = [(1,0), (0,2), (1,1)]
            - visit = [(0,1), (1,0), (0,2), (1,1)]
        - Iteration 4: (-1,0)
            - r,c = (0,1) + (-1,0) = (-1,1)
            - condition not satisfied

        - So this will keep iterating until it doesn't find the cell with value = 0.
        - Ones all the cells with value = 1 are visited it returns to main and increase the cound.
"""

from collections import deque

def bfs(r,c):
    queue = deque()
    visit.add((r,c))
    queue.append((r,c))
    directions = [[0,1], [0,-1], [1,0], [-1,0]]

    while queue:
        r,c = queue.popleft()

        for dr, dc in directions:
            r, c = r+dr, c+dc
            if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visit:
                queue.append((r,c))
                visit.add((r,c))


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    rows = len(grid)
    cols = len(grid[0])
    island = 0
    visit = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visit:
                bfs(r,c)
                island += 1
    print(island)