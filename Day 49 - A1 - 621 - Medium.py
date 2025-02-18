class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxHeap = [-count for count in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        queue = deque() # pairs of [-count, idleTime]

        while maxHeap or queue:
            time += 1
            if maxHeap:
                count = heapq.heappop(maxHeap) + 1
                if count:
                    queue.append([count, time + n])
            if queue and queue[0][1] == time:
                    heapq.heappush(maxHeap ,queue.popleft()[0])
        
        return time