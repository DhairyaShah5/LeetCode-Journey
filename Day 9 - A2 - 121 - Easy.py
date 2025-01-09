class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highestProfit = 0
        minPrice = float('inf')
        
        for price in prices:
            minPrice = min(minPrice, price)
        
            currentProfit = price - minPrice
        
            highestProfit = max(highestProfit, currentProfit)
            
        return highestProfit