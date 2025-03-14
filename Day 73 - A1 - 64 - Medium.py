class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[-1] * COLS for _ in range(ROWS)]

        def dfs(row, col):
            if row == ROWS - 1 and col == COLS - 1:
                return grid[row][col]
            if row == ROWS or col == COLS:
                return float('inf')
            if dp[row][col] != -1:
                return dp[row][col]

            dp[row][col] = grid[row][col] + min(dfs(row + 1, col), dfs(row, col + 1))
            return dp[row][col]

        return dfs(0, 0)