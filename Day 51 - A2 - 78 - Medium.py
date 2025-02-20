class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i):

            if i >= len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[i]) # Case 1, include the nums[i]
            dfs(i + 1)

            subset.pop() # Case 2, do not include the nums[i], hence popped it
            dfs(i + 1)

        dfs(0)

        return result