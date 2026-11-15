class Solution:

    
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(grid, r, c):
            grid[r][c] = "0"
            movementList = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]

            for row, col in movementList:
                if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[row]) and grid[row][col] == "1":
                    dfs(grid, row, col)        

        totalIslands = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):

                if grid[r][c] == "1":
                    totalIslands += 1
                    dfs(grid, r, c)

        return totalIslands
    