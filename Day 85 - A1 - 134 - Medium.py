class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1
        
        remainingFuel = 0
        startStation = 0

        for station in range(len(gas)):
            remainingFuel += (gas[station] - cost[station])
            if remainingFuel < 0:
                remainingFuel = 0
                startStation = station + 1
            
        return startStation