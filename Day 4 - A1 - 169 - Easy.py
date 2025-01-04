class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         i = math.ceil(len(nums)/2) - 1
#         return nums[i]