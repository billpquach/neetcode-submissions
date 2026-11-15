class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # iterate throught each elem in grid
        # if grid[r][c] == 1: search all adjacent land tiles and add to sum
        # res = max(res, currSum)
        # avoid revisting by hash or setting to 0

        #      0 1 2 3 4
        #   0 [0,1,1,0,1],
        #   1 [1,0,1,0,1],
        #   2 [0,1,1,0,1],
        #   3 [0,1,0,0,1]
        # 
        
        def dfs(grid, r, c):
            grid[r][c] = 0
            area = 0
            movementList = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for row, col in movementList:
                if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[row]) and grid[row][col] == 1:
                    area += 1 + dfs(grid, row, col)
            return area
            
            

        currArea, maxArea = 0, 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                currArea = 0
                if grid[r][c] == 1:
                    currArea = 1 + dfs(grid, r, c)
                    maxArea = max(maxArea, currArea)
        return maxArea
                
