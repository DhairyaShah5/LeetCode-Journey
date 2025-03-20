class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        dp = {}
        
        def dfs(left, right):
            if left > right:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]

            even = (right - left) % 2 == 0
            left_ = piles[left] if even else 0
            right_ = piles[right] if even else 0
            dp[(left, right)] = max(dfs(left + 1, right) + left_, dfs(left, right - 1) + right_)

            return dp[(left, right)]

        total = sum(piles)
        aliceScore = dfs(0, len(piles) - 1)
        return aliceScore > total - aliceScore