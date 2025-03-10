class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        currentMinimum, currentMaximum = 1, 1
        for num in nums:
            temp = num * currentMaximum
            currentMaximum = max(num * currentMaximum, num * currentMinimum, num)
            currentMinimum = min(temp, num * currentMinimum, num)
            result = max(result, currentMaximum)

        return result