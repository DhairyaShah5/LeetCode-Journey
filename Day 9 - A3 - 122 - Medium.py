class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                currentProfit = prices[i+1] - prices[i]
                maxProfit += currentProfit
                
        return maxProfit