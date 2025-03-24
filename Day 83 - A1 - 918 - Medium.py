class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax, globalMin = nums[0], nums[0]
        currentMax, currentMin = 0, 0
        total = 0

        for num in nums:
            currentMax = max(currentMax + num, num)
            currentMin = min(currentMin + num, num)
            total += num
            globalMax = max(globalMax, currentMax)
            globalMin = min(globalMin, currentMin)

        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax