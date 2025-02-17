class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        for point in points:
            distance = sqrt(point[0]**2 + point[1]**2)
            result.append((distance, point))

        heapq.heapify(result)

        return [heapq.heappop(result)[1] for _ in range(k)]