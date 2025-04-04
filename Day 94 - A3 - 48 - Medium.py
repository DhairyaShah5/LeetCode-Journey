class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1
        
        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                # Save the topLeft
                topLeft = matrix[top][left + i]

                # Move the bottomLeft to topLeft
                matrix[top][left + i] = matrix[bottom - i][left]

                # Move the bottomRight to bottomLeft
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # Move the topRight to bottomRight
                matrix[bottom][right - i] = matrix[top + i][right]

                # Move the topLeft to topRight
                matrix[top + i][right] = topLeft

            right -= 1
            left += 1