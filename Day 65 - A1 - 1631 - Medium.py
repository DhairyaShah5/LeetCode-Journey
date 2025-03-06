class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])

        visited = set()
        minHeap = [[0, 0, 0]] # Max Abs. Diff., row, column

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            diff, row, column = heapq.heappop(minHeap)

            if (row, column) in visited:
                continue
            visited.add((row, column))
            
            if (row, column) == (ROWS - 1, COLS - 1):
                return diff

            for directionOfRow, directionOfColumn in directions:
                newRow, newColumn = row + directionOfRow, column + directionOfColumn
                if(newRow < 0 or newColumn < 0 or newRow == ROWS or newColumn == COLS or (newRow, newColumn) in visited):
                    continue

                newDiff = max(diff, abs(heights[row][column] - heights[newRow][newColumn]))
                heapq.heappush(minHeap, [newDiff, newRow, newColumn])
                