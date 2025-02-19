class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda trip: trip[1])

        minHeap = [] # Pair of [end, numPassengers]
        currentPassengers = 0

        for numberofPassengers, start, end, in trips:
            while minHeap and minHeap[0][0] <= start:
                currentPassengers -= heapq.heappop(minHeap)[1]

            currentPassengers += numberofPassengers
            if currentPassengers > capacity:
                return False

            heapq.heappush(minHeap, [end, numberofPassengers])

        return True