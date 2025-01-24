class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float('inf')
        left = 0
        sum = 0

        for right in range(len(nums)):
            sum += nums[right]
            
            while sum >= target:
                minLength = min(minLength, right - left + 1)
                sum -= nums[left]
                left += 1
                
        if minLength == float('inf'):
            return 0
        else:
            return minLength