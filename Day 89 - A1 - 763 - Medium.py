class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map = {} # Every character is mapped to it's last index in s

        for index, character in enumerate(s):
            map[character] = index

        result = []
        sizeOfEachPartition, endOfEachPartition = 0, 0
        for index, character in enumerate(s):
            sizeOfEachPartition += 1
            endOfEachPartition = max(endOfEachPartition, map[character])

            if index == endOfEachPartition:
                result.append(sizeOfEachPartition)
                sizeOfEachPartition = 0

        return result