class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        result = right

        def canShip(capacity):
            daysUsed, currCapacity = 1, capacity
            
            for w in weights:
                if currCapacity - w < 0:
                    daysUsed += 1
                    if daysUsed > days:
                        return False
                    currCapacity = capacity
                
                currCapacity -= w
            return True

        while left <= right:
            capacity = left + ((right - left) //2)
            
            if canShip(capacity):
                result = min(result, capacity)
                right = capacity - 1
            else:
                left = capacity + 1
            
        return result