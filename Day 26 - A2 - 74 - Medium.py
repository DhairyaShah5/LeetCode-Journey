class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        columnTop, columnBottom = 0, len(matrix) - 1
        rowLeft, rowRight = 0, len(matrix[0]) - 1

        while columnTop <= columnBottom:
            columnMid = columnTop + ((columnBottom - columnTop) // 2)
            
            if matrix[columnMid][0] <= target <= matrix[columnMid][-1]:
                break
            elif matrix[columnMid][-1] < target:
                columnTop = columnMid + 1
            else:
                columnBottom = columnMid - 1
        else:
            return False

        while rowLeft <= rowRight:
            rowMid = rowLeft + ((rowRight - rowLeft) // 2)
            
            if matrix[columnMid][rowMid] > target:
                rowRight = rowMid - 1
            elif matrix[columnMid][rowMid] < target:
                rowLeft = rowMid + 1
            else:
                return True
        else:
            return False