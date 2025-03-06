class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adjacencyList = { i: [] for i in range(N)}
        
        # Building adjacency List with Manhattan Distance
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]

                distance = abs(x1 - x2) + abs(y1 - y2)
                adjacencyList[i].append([distance, j])
                adjacencyList[j].append([distance, i])

        # Prim's Algorithm
        totalCost = 0
        visited = set()
        minHeap = [[0, 0]] # [Cost, Point]

        while len(visited) < N:
            currentCost, currentPoint = heapq.heappop(minHeap)
            if currentPoint in visited:
                continue

            totalCost += currentCost
            visited.add(currentPoint)
            
            for neighborCost, neighbor in adjacencyList[currentPoint]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, [neighborCost, neighbor])
                
        return totalCost
