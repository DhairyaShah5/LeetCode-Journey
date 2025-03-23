class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximumSubArray, currentSum = nums[0], 0

        for num in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += num
            maximumSubArray = max(maximumSubArray, currentSum)
        
        return maximumSubArray