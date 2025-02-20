class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(i, total):

            if i == len(nums):
                return total
            
            case1 = dfs(i + 1, total ^ nums[i]) # First case we include nums[i]
            case2 = dfs(i + 1, total) # Second case we don't include nums[i]
            sumOfBoth = case1 + case2
            return sumOfBoth

        return dfs(0,0)