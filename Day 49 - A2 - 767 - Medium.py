class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        maxHeap = [[-count, char] for char, count in count.items()]
        heapq.heapify(maxHeap)

        previous = None
        result = ""
        
        while maxHeap or previous:
            if previous and not maxHeap:
                return ""

            count, char = heapq.heappop(maxHeap)
            count += 1
            result += char

            if previous:
                heapq.heappush(maxHeap, previous)
                previous = None

            if count != 0:
                previous = [count, char]
            
        return result