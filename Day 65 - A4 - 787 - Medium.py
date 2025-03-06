class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):  # Iterate for at most k+1 stops
            updatedPrices = prices.copy()  # Temporary price list for this round

            for source, destination, cost in flights:
                if prices[source] == float("inf"):  # Skip unreachable nodes
                    continue
                if prices[source] + cost < updatedPrices[destination]:
                    updatedPrices[destination] = prices[source] + cost

            prices = updatedPrices  # Update prices for the next iteration

        return -1 if prices[dst] == float("inf") else prices[dst]