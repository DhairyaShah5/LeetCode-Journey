class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 1 if n != 0 else 0
        dp = [0] * (n + 1)
        dp[1] = dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]
        
# class Solution:
#     def tribonacci(self, n: int) -> int:
#         t = [0, 1, 1]
        
#         for i in range(3, n + 1):
#             t.append(t[i-1] + t[i-2] + t[i-3])

#         return t[n]        