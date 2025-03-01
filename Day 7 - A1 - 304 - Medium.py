class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMatrix = [[0] * (COLS + 1) for r in range(ROWS +1)]

        for r in range(ROWS):
            prefixSum = 0
            for c in range(COLS):
                prefixSum += matrix[r][c]
                aboveRow = self.sumMatrix[r][c + 1]
                self.sumMatrix[r + 1][c + 1] = prefixSum + aboveRow

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 +1, col2 + 1

        bottomRight = self.sumMatrix[row2][col2]
        aboveRow = self.sumMatrix[row1 - 1][col2]
        leftCol = self.sumMatrix[row2][col1 - 1]
        topLeft = self.sumMatrix[row1 - 1][col1 - 1]

        return bottomRight - aboveRow - leftCol + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)