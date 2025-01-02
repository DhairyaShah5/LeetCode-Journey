class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            x = target - nums[i]
            for y in range(i+1, len(nums)):
                if nums[y] == x:
                    return i,y