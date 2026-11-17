class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def countIsland(i,j):
            if i < 0 or j<0 or i>=len(grid) or j >= len(grid[0]):
                return 0
            if grid[i][j] != 1:
                return 0
            grid[i][j] = 2 
            acc = 0
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                acc += countIsland(i+dx,j+dy)
            return acc + 1

        n = len(grid)
        m = len(grid[0])
        result = 0
        for i in range(n):
            for j in range(m):
                result = max(result, countIsland(i,j))
        return result