class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        n = len(senate)
        direQueue, radiantQueue = deque(), deque()

        for index, character in enumerate(senate):
            if character == "R":
                radiantQueue.append(index)
            else:
                direQueue.append(index)

        while direQueue and radiantQueue:
            direTurn = direQueue.popleft()
            radiantTurn = radiantQueue.popleft()

            if radiantTurn < direTurn:
                radiantQueue.append(radiantTurn + n)
            else:
                direQueue.append(direTurn + n)
        
        return "Radiant" if radiantQueue else "Dire"