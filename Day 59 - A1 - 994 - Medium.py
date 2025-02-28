class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        time = 0

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    fresh += 1
                if grid[row][column] == 2:
                    queue.append((row, column))

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while fresh > 0 and queue:
            length = len(queue)
            for i in range(length):
                row, column = queue.popleft()

                for directionOfRow, directionOfColumn in directions:
                    row_, column_ = row + directionOfRow, column + directionOfColumn

                    if (row_ in range(len(grid)) and column_ in range(len(grid[0])) and grid[row_][column_] == 1):
                        grid[row_][column_] = 2
                        queue.append((row_, column_))
                        fresh -= 1

            time += 1
        return time if fresh == 0 else -1