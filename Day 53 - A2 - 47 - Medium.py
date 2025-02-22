class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutations = []

        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1

        def dfs():
            if len(permutations) == len(nums):
                result.append(permutations.copy())
                return

            for n in count:
                if count[n] > 0:
                    permutations.append(n)
                    count[n] -= 1
                
                    dfs()

                    count[n] += 1
                    permutations.pop()

        dfs()
        return result