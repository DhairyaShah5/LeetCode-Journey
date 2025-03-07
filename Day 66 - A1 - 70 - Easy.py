class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n

#         dp = [0] * (n + 1)
#         dp[1], dp[2] = 1, 2
#         for i in range(3, n + 1):
#             dp[i] = dp[i - 1] + dp[i - 2]
        
#         return dp[n]