class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start, currentCombination):
            if len(currentCombination) == k:
                result.append(currentCombination.copy())

            for i in range(start, n + 1):
                currentCombination.append(i)
                backtrack(i + 1, currentCombination)
                currentCombination.pop()

        backtrack(1, [])
        return result