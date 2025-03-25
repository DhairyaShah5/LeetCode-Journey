class Solution:
    def jump(self, nums: List[int]) -> int:
        result, left, right = 0, 0, 0

        while right < len(nums) - 1:
            furthest = 0
            for i in range(left, right + 1):
                furthest = max(furthest, i + nums[i])

            left = right + 1
            right = furthest
            result += 1
        
        return result