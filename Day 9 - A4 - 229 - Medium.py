class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        tempArray = []
        tempDict = {}

        counter = (len(nums) // 3) + 1

        for num in nums:
            if num in tempDict:
                tempDict[num] += 1
            else:
                tempDict[num] = 1

        for key, value in tempDict.items():
            if value >= counter:
                tempArray.append(key)

        return tempArray