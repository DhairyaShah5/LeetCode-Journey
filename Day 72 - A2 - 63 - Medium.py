class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # Edge case: If the starting or ending cell is blocked, return 0 immediately.
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        # Memoization table initialized with -1
        memo = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            # If out of bounds, return 0
            if i >= m or j >= n:
                return 0
            
            # If there's an obstacle, return 0
            if obstacleGrid[i][j] == 1:
                return 0
            
            # If at the destination, return 1
            if i == m - 1 and j == n - 1:
                return 1

            # If already computed, return stored value
            if memo[i][j] != -1:
                return memo[i][j]

            # Move right and down
            memo[i][j] = dfs(i, j + 1) + dfs(i + 1, j)
            return memo[i][j]

        return dfs(0, 0)