class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(row, col):
            if (row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == "0"):
                return 
            
            grid[row][col] = "0"
            for directionOfRows, directionOfCols in directions:
                dfs(row + directionOfRows, col + directionOfCols)

        for r in range (ROWS):
            for c in range (COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
            
        return islands

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0
        
#         ROWS, COLS = len(grid), len(grid[0])
#         visited = set()
#         islands = 0

#         def bfs(r, c):
#             queue = collections.deque()
#             visited.add((r, c))
#             queue.append((r, c))

#             while queue:
#                 row, col = queue.popleft()
#                 directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # Up, Right, Down, Left
#                 for directionOfRows, directionOfColumns in directions:
#                     rows, columns = row + directionOfRows, col + directionOfColumns
#                     if (rows in range (ROWS) and columns in range (COLS) and grid[rows][columns] == "1" and (rows, columns) not in visited):
#                         queue.append((rows, columns))
#                         visited.add((rows, columns))

#         for r in range (ROWS):
#             for c in range (COLS):
#                 if grid[r][c] == "1" and (r, c) not in visited:
#                     bfs(r, c)
#                     islands += 1

#         return islands