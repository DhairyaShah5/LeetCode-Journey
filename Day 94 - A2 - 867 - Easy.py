class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])
        resultArray = [[0] * ROWS for _ in range(COLS)]

        for r in range(ROWS):
            for c in range(COLS):
                resultArray[c][r] = matrix[r][c]

        return resultArray