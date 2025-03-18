class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(i, targetAmount):
            if targetAmount == amount:
                return 1
            if targetAmount > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, targetAmount) in cache:
                return cache[(i, targetAmount)]

            cache[(i, targetAmount)] = dfs(i, targetAmount + coins[i]) + dfs(i + 1, targetAmount)

            return cache[(i, targetAmount)]
        return dfs(0, 0)