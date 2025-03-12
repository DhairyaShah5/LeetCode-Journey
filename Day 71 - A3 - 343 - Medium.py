class Solution:
    def integerBreak(self, n: int) -> int:
        dp = { 1 : 1 }

        def dfs(num):
            if num in dp:
                return dp[num]

            maxProduct = 0
            for i in range(1, num):
                currentProduct = i * max(num - i, dfs(num - i))
                maxProduct = max(maxProduct, currentProduct)

            dp[num] = maxProduct
            return maxProduct

        return dfs(n)