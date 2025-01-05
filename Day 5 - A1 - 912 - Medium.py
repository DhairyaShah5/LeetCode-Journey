class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(array, LEFT, MIDDLE, RIGHT):
            left_subarray, right_subarray = array[LEFT:MIDDLE+1], array[MIDDLE+1:RIGHT+1]
            
            i, j, k = LEFT, 0, 0

            while j < len(left_subarray) and k < len(right_subarray):
                if left_subarray[j] <= right_subarray[k]:
                    array[i] = left_subarray[j]
                    j += 1
                else:
                    array[i] = right_subarray[k]
                    k += 1
                i += 1
            while j < len(left_subarray):
                array[i] = left_subarray[j]
                j += 1
                i += 1
            while k < len(right_subarray):
                array[i] = right_subarray[k]
                k += 1
                i += 1
                
        def mergeSort(array, left, right):
            if left == right:
                return array
            
            middle = (left + right) // 2
            mergeSort(array, left, middle)
            mergeSort(array, middle + 1, right)
            merge(array, left, middle, right)
            return array

        return mergeSort(nums, 0, len(nums) - 1)
