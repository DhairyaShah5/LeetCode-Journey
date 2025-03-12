class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        
        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])
        
        return dp[n]
        
# class Solution:
#     def numSquares(self, n: int) -> int:
#         memo = {}
#         def dfs(target):
#             if target == 0:
#                 return 0

#             if target in memo:
#                 return memo[target]

#             result = target
#             for i in range(1, target):
#                 if i * i > target:
#                     break
                
#                 result = min(result, 1 + dfs(target - (i * i)))
#                 memo[target] = result
#             return result

#         return dfs(n)