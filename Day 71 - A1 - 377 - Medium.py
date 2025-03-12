class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = { 0 : 1 }

        def dfs(total):
            if total in memo:
                return memo[total]
            
            result = 0
            for i in range(len(nums)):
                if total < nums[i]:
                    break
                result += dfs(total - nums[i])

            memo[total] = result

            return result

        return dfs(target)