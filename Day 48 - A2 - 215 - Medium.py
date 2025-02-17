class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]

        heapq.heapify(nums)

        for _ in range(k):
            kthDistinctElement = -heapq.heappop(nums)

        return kthDistinctElement