class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for source, target, weight in times:
            graph[source].append((target, weight))

        minHeap = [(0, k)]
        visited = set()
        maxTime = 0

        while minHeap:
            currentTime, currentNode = heapq.heappop(minHeap)
            if currentNode in visited:
                continue
            visited.add(currentNode)
        
            maxTime = currentTime

            for neighbor, travelTime in graph[currentNode]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (currentTime + travelTime, neighbor))

        return maxTime if len(visited) == n else -1