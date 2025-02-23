class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(row, column, i):
            if i == len(word):
                return True

            if (row < 0 or column < 0 or
                row >= ROWS or column >= COLS or
                (row, column) in path or
                word[i] != board[row][column]):
                return False

            path.add((row, column))
            result = (dfs(row + 1, column, i + 1) or
                      dfs(row - 1, column, i + 1) or
                      dfs(row, column + 1, i + 1) or
                      dfs(row, column - 1, i + 1))
            path.remove((row, column))

            return result

        for row in range(ROWS):
            for column in range(COLS):
                if dfs(row, column, 0):
                    return True

        return False