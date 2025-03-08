class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMax = 0  # Max money that can be robbed up to the house before the previous one
        currMax = 0  # Max money that can be robbed up to the previous house

        for amount in nums:
            newMax = max(amount + prevMax, currMax)  # Either rob this house or skip it
            prevMax = currMax  # Move forward: previous house becomes the one before the previous
            currMax = newMax  # Update the max amount robbed so far
        
        return currMax

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         memo = [-1] * len(nums)

#         def dfs(i):
#             if i >= len(nums):
#                 return 0
#             if memo[i] != -1:
#                 return memo[i]
            
#             memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
#             return memo[i]
        
#         return dfs(0)        