class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left, right = 0, 1
        result, previousSign = 1, ""

        while right < len(arr):
            if arr[right - 1] > arr[right] and previousSign != ">":
                result = max(result, right - left + 1)
                right += 1
                previousSign = ">"
            
            elif arr[right - 1] < arr[right] and previousSign != "<":
                result = max(result, right - left + 1)
                right += 1
                previousSign = "<"

            else:
                right = right + 1 if arr[right] == arr[right - 1] else right
                left = right - 1
                previousSign = ""

        return result