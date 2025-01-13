class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueElements = sorted(set(nums))
        nums[:len(uniqueElements)] = uniqueElements
        return len(uniqueElements)
        