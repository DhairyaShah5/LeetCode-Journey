class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = deque([0])
        furthest = 0

        while queue:
            i = queue.popleft()
            start = max(i + minJump, furthest + 1)
            for j in range(start, min(i + maxJump + 1, len(s))):
                if s[j] == "0":
                    queue.append(j)
                    if j == len(s) - 1:
                        return True
            
            furthest = i + maxJump
        
        return False
        