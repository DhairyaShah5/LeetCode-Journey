class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
# Since Python does not have maxHeap, we can convert the stones list into negative stones list which will help us in implementation of the minHeap as maxHeap, while returning just be careful to convert the negative values back to it's original positive state, since weight can not be negative

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            firstStone = heapq.heappop(stones)
            secondStone = heapq.heappop(stones)

            if secondStone > firstStone:
                heapq.heappush(stones, firstStone - secondStone)
            
        return -stones[0] if stones else 0