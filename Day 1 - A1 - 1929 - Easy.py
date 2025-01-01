class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums
        
# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         return nums + nums