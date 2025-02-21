class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        for n in nums:
            newPermutations = []
            for p in permutations:
                for i in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(i, n)
                    newPermutations.append(pCopy)

            permutations = newPermutations
        return permutations

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         if len(nums) == 0:
#             return [[]]

#         permutations = self.permute(nums[1:])

#         for p in permutations:
#             for i in range(len(p) + 1):
#                 pCopy = p.copy()
#                 pCopy.insert(i, nums[0])
#                 result.append(pCopy)

#         return result