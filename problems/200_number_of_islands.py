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