class Solution:
    def rob(self, nums: List[int]) -> int:

        return max(nums[0], self.helper(nums[1:]), self.helper(nums[: -1]))        

    def helper(self, nums):
        prevMax = 0  # Max money that can be robbed up to the house before the previous one
        currMax = 0  # Max money that can be robbed up to the previous house

        for amount in nums:
            newMax = max(amount + prevMax, currMax)  # Either rob this house or skip it
            prevMax = currMax  # Move forward: previous house becomes the one before the previous
            currMax = newMax  # Update the max amount robbed so far
        
        return currMax